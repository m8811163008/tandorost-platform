
from pydantic import BaseModel, ConfigDict
from domain_models.data_models import GallaryTag


class UserStaticFiles(BaseModel):
    profile_image : list[str]
    image_gallery : dict[str | GallaryTag, list[str]]
    model_config = ConfigDict(use_enum_values=True,)



