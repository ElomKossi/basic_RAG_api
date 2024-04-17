from pydantic import BaseModel, Field

from app.chats.constants import ChatRolesEnum, ModelsEnum
from app.core.models import TimestampAbstractModel


class BaseMessage(BaseModel):
    """ Base pydantic model that we use to interact with the API."""
    model: ModelsEnum = Field(default=ModelsEnum.GPT3.value)
    message: str


class Message(TimestampAbstractModel, BaseMessage):
    role: ChatRolesEnum



class Message(BaseMessage):
    role: ChatRolesEnum