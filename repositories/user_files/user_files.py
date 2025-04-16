

from data.local_database import DatabaseInterface
from data.local_database.model.user_files import GallaryTag, UserStaticFiles

class UserFiles:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user_profile_image(self,  user_id:str) -> str | None:
        return await self.database.read_user_profile_image(user_id=user_id)

    async def read_user_image_gallary(self,  user_id:str, tags:list[str | GallaryTag]) -> dict[str | GallaryTag, list[str]] | None:
        return await self.database.read_user_image_gallary(user_id=user_id, tags=tags)


    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        return await self.database.upsert_user_files(user_files = user_files)