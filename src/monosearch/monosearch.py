from .datatypes.common import LlmConfig, SearchContext
from .query_analyzer import LLMQueryAnalyzer
from .retriever import BochaRetriever
from .ranker import LLMRanker
from .reflex import Reflex
from .summarizer import Summarizer


class MonoSearch:
    def __init__(
        self,
        query_analyzer=None,
        retriever=None,
        ranker=None,
        reflex=None,
        summarizer=None
    ):
        self.query_analyzer = query_analyzer or LLMQueryAnalyzer()
        self.retriever = retriever or BochaRetriever()
        self.ranker = ranker or LLMRanker()
        self.reflex = reflex or Reflex()
        self.summarizer = summarizer or Summarizer()

    def search(self, query: str, llm_config: LlmConfig = LlmConfig(), max_iterations: int = 10) -> str:
        
        context = SearchContext(
            user_query = query,
            llm_config = llm_config
        )
        
        # Query理解
        query_list = self.query_analyzer.analyze(query, context)
        
        iteration = 0
        while context.current_queries and iteration < max_iterations:
            iteration += 1
            # 召回
            query_documents = self.retriever.retrieve(query_list, context)
            # 排序
            rank_documents = self.ranker.rank(query_documents, context)
            # 反思
            should_continue, query_list = self.reflex.reflect(rank_documents, context)

            if not should_continue:
                break
        
        # 总结
        return self.summarizer.summarize(context)