
from pydantic import   BaseModel, Field, ConfigDict

class Token(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    access_token: str
    token_type: str
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


class TokenData(BaseModel):
    username: str | None = None

