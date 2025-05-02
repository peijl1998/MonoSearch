
from ..datatypes.common import Document, SearchContext
from .base_retriever import BaseRetriever
from ..ability.search.bocha_search import search_bocha
from ..utils.model_adapter import bocha_to_query_documents
from typing import List


class BochaRetriever(BaseRetriever):
    def __init__(self, count: int = 5, page: int = 1):
        self.count = count
        self.page = page
        
    def retrieve_single(self, query: str, context: SearchContext) -> List[Document]:
        try:
            response = search_bocha(query, count=self.count, page=self.page)
            return bocha_to_query_documents(response)
        except Exception as e:
            print(f"Bocha Retriever Error: {e}")
            return []