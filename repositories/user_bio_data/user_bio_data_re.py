

from data.local_database import DatabaseInterface
from domain_models import ObjectId, UserBioData

class UserBioDataRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database


    async def upsert_user_bio_data(self,user_bio_data: UserBioData, user_id : ObjectId | None = None, )-> UserBioData:
        if user_id == None:
            id = await self.database.create_user_bio_data(user_bio_data=user_bio_data)
            created_user_bio_data = await self.database.read_user_bio_data(user_id= id)
            assert(created_user_bio_data != None)
            return created_user_bio_data
        else:
            return await self.database.update_user_bio_data(user_id=user_id, user_bio_data=user_bio_data)

    
    async def read_user_bio_data(self, user_id:ObjectId) -> UserBioData | None:
        """Read user data"""
        pass