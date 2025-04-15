from enum import Enum
from pydantic import BaseModel, Field,ConfigDict


class GallaryTag(Enum):
    DEFAULT = 'default'
    CERTIFICATE = 'certificate'

class UserStaticFiles(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    profile_image : list[str]
    image_gallery : dict[str | GallaryTag, list[str]]
    model_config = ConfigDict(use_enum_values=True,)




