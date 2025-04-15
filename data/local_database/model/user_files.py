from enum import Enum
from pydantic import UUID4, BaseModel, Field,ConfigDict,field_serializer
from uuid import uuid4

class GallaryTag(Enum):
    DEFAULT = 'default'
    CERTIFICATE = 'certificate'

class UserStaticFiles(BaseModel):
    id : UUID4 = Field(alias="_id", default= uuid4())
    user_id : UUID4
    profile_image : list[str]
    image_gallery : dict[str | GallaryTag, list[str]]
    model_config = ConfigDict(use_enum_values=True,
                              arbitrary_types_allowed = True
                              )

    @field_serializer('id')
    def serialize_id(self, id: UUID4) -> str:
        return str(id)
    
    @field_serializer('user_id')
    def serialize__user_id(self, id: UUID4) -> str:
        return str(id)


