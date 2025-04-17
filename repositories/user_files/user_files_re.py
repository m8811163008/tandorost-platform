


from data.local_database import DatabaseInterface

from domain_models.data_models import FileMetaData, GallaryTag, UserStaticFiles

class UserFiles:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user_profile_image(self,  user_id:str) -> FileMetaData | None:
        profile_images = await self.database.read_user_image_gallary(user_id=user_id, tags=[GallaryTag.PROFILE_IMAGE])
        if profile_images is None:
            return None
        return profile_images[GallaryTag.PROFILE_IMAGE][-1]

    async def read_user_image_gallary(self,  user_id:str, tags:list[str | GallaryTag]) -> dict[str | GallaryTag, list[FileMetaData]] | None:
        return await self.database.read_user_image_gallary(user_id=user_id, tags=tags)
    
    async def read_user_static_files(self,  user_id:str) -> UserStaticFiles | None:
        return await self.database.read_user_static_files(user_id=user_id)

    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        return await self.database.upsert_user_files(user_files = user_files)