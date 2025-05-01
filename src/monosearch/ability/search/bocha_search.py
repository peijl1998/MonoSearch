import requests
import json
from monosearch.datatypes.search_api_response import BochaResponse
from monosearch.utils.secret_holder import get_bocha_api_key

url = "https://api.bochaai.com/v1/web-search"

def search_bocha(query: str, count: int = 10, page: int = 1) -> BochaResponse:
    payload = json.dumps({
      "query": query,
      "summary": True,
      "count": count,
      "page": page
    })

    headers = {
      'Authorization': f'Bearer {get_bocha_api_key()}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return BochaResponse.model_validate(response.json())