from pydantic import BaseModel


class UserFoodCount(BaseModel):
    count: int