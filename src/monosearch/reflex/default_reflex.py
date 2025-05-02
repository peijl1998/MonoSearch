from typing import List, Tuple
from monosearch.ability.llm import silicon_flow
from monosearch.datatypes.common import SearchContext
from .base_reflex import BaseReflex


REFLEX_PROMPT = """
根据用户的搜索需求以及已经查询到的相关结果，从全面、深度出发，请给出进一步子查询列表，如果已经足够回答用户需求，请返回空列表。
这是深度搜索场景，除非非常确认满足用户诉求，否则请务必给出子查询，以确保能够准确回答用户需求。

# 输入
<user_query>{query}</user_query>
<search_results>
{search_results}
</search_results>

# 输出格式
python的str列表，务必遵守。
"""

class DefaultReflex(BaseReflex):
    def reflect(self, context: SearchContext) -> Tuple[bool, List[str]]:
        all_queries = context.intermediate_results.getAllKeywords()
        
        search_results = ""
        for keyword, docs in context.intermediate_results.results.items():
            search_results += f"子查询：{keyword}\n"
            for i, doc in enumerate(docs):
                search_results += f"序号{i} 内容：{doc.content}\n"
                
        prompt = REFLEX_PROMPT.format(
            query=context.user_query,
            search_results=search_results
        )
        response = silicon_flow.chat(prompt, context.llm_config)
        
        new_queries = []
        try:
            new_queries = eval(response.choices[0].message.content)
            new_queries = [q for q in new_queries if q not in all_queries]
        except:
            new_queries = []
        
        if new_queries:
            return True, new_queries
        else:
            return False, []
        