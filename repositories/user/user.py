

from data.local_database import DatabaseInterface
from data.local_database.model.user_physical_data import UserPhysicalData
from domain_models import  UserInDB, UserPhysicalDataUpsert

class UserRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user(self, user_id : str) -> UserInDB | None:
        """Retrieve a user from the database."""
        return await self.database.read_user_by_id(
            user_id = user_id
        )
    
    async def update_user(self, user : UserInDB)-> UserInDB | None:
        """Retrieve a user from the database."""
        assert(user.id is not None)
        return await self.database.upsert_user(
            user=user
        )
    
    async def read_user_physical_data(self, user_id:str) -> UserPhysicalData | None:
        return await self.database.read_user_physical_data(user_id = user_id)
    
    async def upsert_user_physical_data(self,user_id :str ,user_physical_data: UserPhysicalDataUpsert )-> UserPhysicalData:
        return await self.database.upsert_user_physical_data(user_physical_data=user_physical_data, user_id = user_id)
    

    async def delete_user_physical_data(self,user_id : str, data_point_id : str):
        await self.database.delete_user_physical_data(user_id = user_id, data_point_id=data_point_id)
