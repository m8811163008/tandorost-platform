
from pydantic import BaseModel, ConfigDict
from domain_models.data_models import GallaryTag, FileMetaData


class UserStaticFilesResponse(BaseModel):
    profile_image : FileMetaData | None = None
    image_gallery : dict[str | GallaryTag, list[FileMetaData]] | None = None
    model_config = ConfigDict(use_enum_values=True,)



