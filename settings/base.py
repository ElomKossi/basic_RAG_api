from pydantic import Field
from pydantic_settings import BaseSettings

from app.core.constants import Environments


class Settings(BaseSettings):
    APP_NAME: str = "bRAG"
    ENVIRONMENT: str = Field(env="ENVIRONMENT", default=Environments.LOCAL.value)
    OPENAI_API_KEY: str = Field(env="OPENAI_API_KEY")

    @property
    def is_local(self):
        return self.ENVIRONMENT == Environments.LOCAL.value

    # this will make it so that pydantic will look for our env variables
    # in a file called .env and automatically load them as such
    class Config:
        env_file = ".env"