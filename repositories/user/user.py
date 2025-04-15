

from pydantic import UUID4
from data.local_database import DatabaseInterface
from data.local_database.model.user_bio_data import UserBioData
from domain_models import  UserInDB

class UserRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user(self, user_id : UUID4) -> UserInDB | None:
        """Retrieve a user from the database."""
        return await self.database.read_user_by_id(
            user_id = str(user_id) 
        )
    
    async def update_user(self, user : UserInDB)-> UserInDB | None:
        """Retrieve a user from the database."""
        return await self.database.upsert_user(
            user=user
        )
    
    async def read_user_bio_data(self, user_id:UUID4) -> UserBioData | None:
        return await self.database.read_user_bio_data(user_id = str(user_id))
    
    async def upsert_user_bio_data(self,user_bio_data: UserBioData, user_id : UUID4 )-> UserBioData:
        return await self.database.upsert_user_bio_data(user_id=str(user_id), user_bio_data=user_bio_data)
            

    
