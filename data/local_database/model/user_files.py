from enum import Enum
from pydantic import UUID4, BaseModel, Field,ConfigDict
from uuid import uuid4

class GallaryTag(Enum):
    DEFAULT = 'default'
    CERTIFICATE = 'certificate'

class UserStaticFiles(BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4(), exclude= True)
    user_id : UUID4
    profile_image : list[str]
    image_gallery : dict[str | GallaryTag, list[str]]
    model_config = ConfigDict(use_enum_values=True,
                              arbitrary_types_allowed = True
                              )




