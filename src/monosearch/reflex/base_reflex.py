from typing import List, Tuple
from abc import ABC, abstractmethod

from ..datatypes.common import SearchContext


class BaseReflex(ABC):
    @abstractmethod
    def reflect(self, context: SearchContext) -> Tuple[bool, List[str]]:
        pass