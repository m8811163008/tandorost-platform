
from pydantic import  UUID4, BaseModel, Field, ConfigDict
from uuid import uuid4
class Token(BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4())
    user_id : UUID4
    access_token: str
    token_type: str
    model_config = ConfigDict(use_enum_values=True,
                              arbitrary_types_allowed = True
                              )


class TokenData(BaseModel):
    username: str | None = None

