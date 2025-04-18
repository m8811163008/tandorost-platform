from pydantic import BaseModel


class ArchiveUserImagesResponse(BaseModel):
    updated_images_ids: list[str]
    images_id: list[str]