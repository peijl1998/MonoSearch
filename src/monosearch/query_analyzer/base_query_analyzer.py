from typing import List
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext


class BaseQueryAnalyzer(ABC):    
    @abstractmethod
    def analyze(self, query: str, context: SearchContext) -> List[str]:
        pass

