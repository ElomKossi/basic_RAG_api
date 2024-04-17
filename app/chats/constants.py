# chat/constants.py
from enum import StrEnum


class FailureReasonsEnum(StrEnum):
    OPENAI_ERROR = "OpenAI call failed"
    STREAM_TIMEOUT = "Stream timed out"  # for later
    FAILED_PROCESSING = "Post processing failed"  # for later


class ChatRolesEnum(StrEnum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"


class ModelsEnum(StrEnum):
    GPT3 = "gpt-3.5-turbo"
    
NO_DOCUMENTS_FOUND: str = (
    "No documents found in context. Please try again with a different query."
)