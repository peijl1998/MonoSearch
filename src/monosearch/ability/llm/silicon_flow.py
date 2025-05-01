import requests

from monosearch.datatypes.common import LlmConfig
from monosearch.datatypes.llm_api_response import LLMAPIResponse
from monosearch.utils.secret_holder import get_silicon_flow_api_key

url = "https://api.siliconflow.cn/v1/chat/completions"

def chat(query: str, config: LlmConfig) -> LLMAPIResponse:
    messages = [{
            "role": "user",
            "content": query
        }
    ]
    
    payload = {
        "model": config.model_name,
        "messages": messages,
        "stream": False,
        "enable_thinking": False
    }
    headers = {
        "Authorization": f"Bearer {get_silicon_flow_api_key()}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return LLMAPIResponse.model_validate(response.json())
    