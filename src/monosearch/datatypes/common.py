from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str
    content: str


class Memory(BaseModel):
    history: List[Message]
    
    def addMessage(self, message: Message):
        self.history.append(message)


class LlmConfig(BaseModel):
    model_name: str = "Qwen/Qwen3-8B"


class DocumentSource(str, Enum):
    BOCHA = "bocha"
    UNKNOWN = "unknown"


class Document(BaseModel):
    id: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    source: DocumentSource = DocumentSource.UNKNOWN
    url: Optional[str] = None
    title: Optional[str] = None


class SearchResult(BaseModel):
    user_query: str
    result: Optional[str] = None


class SearchContext(BaseModel):
    user_query: str
    llm_config: LlmConfig = Field(default_factory=LlmConfig)


class QueryDocuments(BaseModel):
    results: Dict[str, List[Document]] = Field(default_factory=dict)
    
    def addDocument(self, keyword: str, document: Document) -> None:
        if keyword not in self.results:
            self.results[keyword] = []
            
        if document.id not in [doc.id for doc in self.results[keyword]]:
            self.results[keyword].append(document)
    
    def addDocuments(self, keyword: str, documents: List[Document]) -> None:
        for doc in documents:
            self.addDocument(keyword, doc)
    
    def addResult(self, other: 'QueryDocuments') -> None:
        for keyword, docs in other.results.items():
            self.addDocuments(keyword, docs)
    
    def getDocuments(self, keyword: str) -> List[Document]:
        return self.results.get(keyword, [])
            
    def getAllKeywords(self) -> List[str]:
        return list(self.results.keys())