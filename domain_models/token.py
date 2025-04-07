from uuid import UUID
from pydantic import BaseModel, Field

class Token(BaseModel):
    id : UUID | None = Field(alias="_id", default=None)
    user_id : UUID
    access_token: str
    token_type: str



class TokenData(BaseModel):
    username: str | None = None

