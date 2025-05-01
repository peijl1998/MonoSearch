from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext, Document


class BaseSummarizer(ABC):
    
    @abstractmethod
    def summarize(self, context: SearchContext) -> str:
        pass
