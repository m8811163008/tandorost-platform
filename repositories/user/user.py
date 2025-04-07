from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any

from domain_models.user import User, UserInDB

class UserRepository:
    def __init__(self, uri: str, database_name: str):
        self.client: Any = AsyncIOMotorClient(uri)
        self.db = self.client[database_name]
        self.collection = self.db["users"]

    async def save_user(self, user: UserInDB) -> UUID:
        """Save a user token to the database."""
        user_data = user.model_dump()
        await self.collection.insert_one(user_data)
        assert(user.id is not None)
        return user.id

    async def get_user(self, user_name: str) -> User | None:
        """Retrieve a user token from the database."""
        user_data = await self.collection.find_one({"username": user_name})
        if user_data:
            return UserInDB(**user_data)
        return None