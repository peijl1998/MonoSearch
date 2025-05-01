from .base_ranker import BaseRanker
from ..datatypes.common import QueryDocuments, SearchContext, Document
from ..ability.llm import silicon_flow
from ..utils.thread_pool import ThreadPool


RANK_PROMPT = """
## Role
你是一个搜索引擎的排序专家，能够从召回文档结果中筛选出和关键词相关的内容并排序。

## 输出格式
文档下标构成的python列表（从0开始），例如[1,3,5]

## 输入
搜索关键词：{query}
召回文档片段：{documents}

## Constrains
1、输出格式一定要是python列表，如果没有相关，可以输出[]
"""


class LLMRanker(BaseRanker):
    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
    
    def rank(self, query_documents: QueryDocuments, context: SearchContext) -> QueryDocuments:    
        result = QueryDocuments()
        
        # 并行处理每个query的召回结果
        ranked_docs_dict = ThreadPool.map_with_key(
            lambda docs: self._rank_single_query(docs[0], docs[1], context),
            {query: (query, docs) for query, docs in query_documents.results.items()},
            max_workers=self.max_workers
        )
        
        for query, ranked_docs in ranked_docs_dict.items():
            result.results[query] = ranked_docs
            
        return result
    
    def _rank_single_query(self, query: str, documents: list, context: SearchContext) -> list:
        prompt = RANK_PROMPT.format(
            query=query,
            documents="\n".join([f"序号:{i}  内容:{doc.content}" for i, doc in enumerate(documents)])
        )
        response = silicon_flow.chat(prompt, context.llm_config)
        try:
            indices = eval(response.choices[0].message.content)
            print(len(documents), len(indices), indices)
            return [documents[i] for i in indices]
        except:
            return []
