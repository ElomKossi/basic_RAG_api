from datetime import datetime

from pydantic import BaseModel, Field


# utility base class to add creation time to all the models
# usually we would also have updated_at field to denote
# when the object was updated, but in our case I doubt we will do
# any updatescd ..
class TimestampAbstractModel(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)