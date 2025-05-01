from typing import List
from .base_query_analyzer import BaseQueryAnalyzer
from ..datatypes.common import SearchContext
from ..ability.llm import silicon_flow


ANALYZE_PROMPT = """
# Role
你是一个专业搜索专家，接下来为了全面回答用户的问题，需要将其查询分解为多个子查询（最多5个），如果用户的问题已经很简单则不需要分解，保留原始问题即可。

# 输入
<user_query>{query}</user_query>

# 输出格式
Python代码列表格式，例如["查询1","查询2"]
"""


class LLMQueryAnalyzer(BaseQueryAnalyzer):    
    def analyze(self, query: str, context: SearchContext) -> List[str]:
        prompt = ANALYZE_PROMPT.format(query=query)
        response = silicon_flow.chat(prompt, context.llm_config)
        try:
            keywords = eval(response.choices[0].message.content)
            return keywords if isinstance(keywords, list) and all(isinstance(k, str) for k in keywords) else [query]
        except:
            return [query]