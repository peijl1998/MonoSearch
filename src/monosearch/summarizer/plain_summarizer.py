
from monosearch.ability.llm import silicon_flow
from monosearch.datatypes.common import SearchContext
from .base_summarizer import BaseSummarizer


SUMMARIZE_PROMPT = """
你是一个专业的信息总结专家，针对用户的搜索请求，你已经分解多个子查询并得到相关结果，你需要根据这些内容对用户原始查询作出最终答复。
以下是相关信息
<user_query>{query}</user_query>
<search_results>
{search_results}
</search_results>
"""

class PlainSummarizer(BaseSummarizer):
    def summarize(self, context: SearchContext) -> str:
        search_results = ""
        for keyword, docs in context.intermediate_results.results.items():
            search_results += f"子查询：{keyword}\n"
            for i, doc in enumerate(docs):
                search_results += f"序号{i} 内容：{doc.content}\n"
                
        prompt = SUMMARIZE_PROMPT.format(
            query=context.user_query,
            search_results=search_results
        )
        response = silicon_flow.chat(prompt, context.llm_config)
        return response.choices[0].message.content

