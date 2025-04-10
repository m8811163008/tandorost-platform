from bson import ObjectId
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from typing import Any
from uuid import UUID
from pymongo import ReturnDocument
from data.local_database import (
    DatabaseInterface, 
    Token
)
from domain_models import (DocumentNotFound, UserInDB)


class LocalDataBaseImpl(DatabaseInterface):
    def __init__(self, uri: str, database_name: str):
        self.client: AsyncIOMotorClient[dict[str,Any]] = AsyncIOMotorClient(uri)
        self.db :AsyncIOMotorDatabase[dict[str,Any]] = self.client[database_name]
        self.user_collection : AsyncIOMotorCollection[dict[str,Any]] = self.db["users"]
        self.auth_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["tokens"]

    async def clear(self):
        await self.user_collection.delete_many({})
        await self.auth_collection.delete_many({})
        print('*****Database cleared!*****')

    async def create_user(self, user: UserInDB) -> str:
        """Save a user token to the database."""
        result = await self.user_collection.insert_one(
            user.model_dump(by_alias=True, exclude={"id"})
        )
        return result.inserted_id
    
    async def update_user(self, id:str , user: UserInDB)-> UserInDB:
        user_dict = {
            k: v for k, v in user.model_dump(by_alias=True).items() if v is not None
        }
        if len(user_dict) >= 1:
            update_result = await self.user_collection.find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": user_dict},
                return_document=ReturnDocument.AFTER,
            )
            if len(update_result) != 0:
                return UserInDB(**update_result)
            else:
                raise DocumentNotFound()
        # The update is empty, but we should still return the matching document:
        existing_user = await self.user_collection.find_one({"_id": id})
        if existing_user is not None:
            return UserInDB(**existing_user)
        raise DocumentNotFound()


    async def read_user(self, username:str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"username": username})
        if user_data is None:
            return None
        return UserInDB(**user_data)

    # Auth methods
    async def save_token(self, token: Token, user_id : ObjectId) -> Token:
        """Save a user token to the database."""
        issued_token = await self.auth_collection.find_one_and_update(
            filter={'user_id': user_id},
            update={'$set': token.model_dump(by_alias=True,exclude={'id'})},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return Token(**issued_token)


    async def get_token(self, id: UUID) -> Token | None:
        """Retrieve a user token from the database."""
        token_data = await self.auth_collection.find_one({"_id": id})
        if token_data:
            return Token(**token_data)
        return None