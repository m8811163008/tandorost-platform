
from pydantic import  BaseModel, Field,ConfigDict


class Coach(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    biography: str | None = None
    is_active : bool | None = None
    model_config = ConfigDict(use_enum_values=True)