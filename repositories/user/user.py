from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from typing import Any

from domain_models.exceptions import UsernameAlreadyInUse
from domain_models.user import UserInDB

class UserRepository:
    def __init__(self, uri: str, database_name: str):
        self.client: AsyncIOMotorClient[dict[str,Any]] = AsyncIOMotorClient(uri)
        self.db :AsyncIOMotorDatabase[dict[str,Any]] = self.client[database_name]
        self.collection : AsyncIOMotorCollection[dict[str,Any]] = self.db["users"]
        self.testVar : str

    async def save_user(self, user: UserInDB) -> UserInDB:
        """Save a user token to the database."""
        current_user = await self.collection.find_one(
            {"username": user.username}
        )
        if current_user is not None:
            raise UsernameAlreadyInUse() 
        result = await self.collection.insert_one(
            user.model_dump(by_alias=True, exclude={"id"})
        )
        
        saved_user = await self.collection.find_one(
            {"_id": result.inserted_id}
        )
        assert(saved_user is not None)
        return UserInDB(**saved_user)

    async def get_user(self, user_name: str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.collection.find_one({"username": user_name})
        if user_data:
            return UserInDB(**user_data)
        return None