from enum import Enum
from pydantic import BaseModel, Field

from data.local_database.model.pydantic_object_id import ObjectId

class GallaryTag(Enum):
    DEFAULT = 'default'
    CERTIFICATE = 'certificate'

class UserStaticFiles(BaseModel):
    id : ObjectId | None = Field(alias="_id", default= None, exclude= True)
    user_id : ObjectId
    profile_image : list[str]
    image_gallery : dict[str | GallaryTag, list[str]]




