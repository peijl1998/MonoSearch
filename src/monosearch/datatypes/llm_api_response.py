from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str
    content: str


class TokenUsageDetails(BaseModel):
    reasoning_tokens: int = 0


class TokenUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    completion_tokens_details: Optional[TokenUsageDetails] = None


class CompletionChoice(BaseModel):
    index: int
    message: Message
    finish_reason: str


class LLMAPIResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[CompletionChoice]
    usage: TokenUsage
    system_fingerprint: str = ""
