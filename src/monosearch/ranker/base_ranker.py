from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext, Document, QueryDocuments

class BaseRanker(ABC):
    @abstractmethod
    def rank(self, query_documents: QueryDocuments, context: SearchContext) -> QueryDocuments:
        pass

class DefaultRanker(BaseRanker):
    def rank(self, query_documents: QueryDocuments, context: SearchContext) -> QueryDocuments:
        return query_documents
