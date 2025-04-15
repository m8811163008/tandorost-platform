
from fastapi.types import IncEx
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from typing import Any

from pymongo import ReturnDocument
from data.local_database import Token
from data.local_database.local_database_interface import DatabaseInterface
from data.local_database.model.exceptions import DocumentNotFound
from data.local_database.model.user import UserInDB
from data.local_database.model.user_bio_data import UserBioData
from data.local_database.model.user_files import UserStaticFiles
from bson import ObjectId


class LocalDataBaseImpl(DatabaseInterface):
    def __init__(self, uri: str, database_name: str):
        self.client: AsyncIOMotorClient[dict[str,Any]] = AsyncIOMotorClient(uri)
        self.db :AsyncIOMotorDatabase[dict[str,Any]] = self.client[database_name]
        self.user_collection : AsyncIOMotorCollection[dict[str,Any]] = self.db["UserCollection"]
        self.auth_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["TokenCollection"]
        self.user_bio_data_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserBioDataCollection"]
        self.user_static_file_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserStaticsFileCollection"]

    def _exclude_id(exclude: IncEx | None) : # type: ignore
        return (exclude or set()).union({"id"}) # type: ignore
    
    async def clear(self):
        await self.user_collection.delete_many({})
        await self.auth_collection.delete_many({})
        print('*****Database cleared!*****')

    async def read_user(self, username:str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"phone_number": username})
        if user_data is None:
            return None
        return UserInDB(**user_data)
    
    async def read_user_by_id(self, user_id : ObjectId) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            return None
        return UserInDB(**user_data)

    async def create_user(self, user: UserInDB) -> ObjectId:
        """Save a user token to the database."""
        result = await self.user_collection.insert_one(
            user.model_dump(by_alias=True)
        )
        return result.inserted_id
    
    async def update_user(self, id:ObjectId , user: UserInDB)-> UserInDB:
        user_dict = {
            k: v for k, v in user.model_dump(by_alias=True).items() if v is not None # type: ignore
        }
        if len(user_dict) >= 1:
            update_result = await self.user_collection.find_one_and_update(
                {"_id": id},
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


    async def create_user_bio_data(self, user_bio_data: UserBioData)-> ObjectId:
        """Retrieve a user token from the database."""
        result = await self.user_bio_data_collection.insert_one(
            user_bio_data.model_dump(by_alias=True)
        )
        return result.inserted_id
        

    async def update_user_bio_data(self, user_id : ObjectId, user_bio_data: UserBioData, exclude: IncEx | None = None)-> UserBioData:
        """Update user data"""
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            raise DocumentNotFound()
        user_dict = {
            k: v for k, v in user_bio_data.model_dump(by_alias=True, exclude= _exclude_id(exclude)).items() if v is not None # type: ignore
        }
        if len(user_dict) >= 1:
            update_result = await self.user_bio_data_collection.find_one_and_update(
                {"user_id": user_id},
                {"$set": user_dict},
                return_document=ReturnDocument.AFTER,
            )
            if len(update_result) != 0:
                return UserBioData(**update_result)
            else:
                raise DocumentNotFound()
        # The update is empty, but we should still return the matching document:
        existing_user_bio_data = await self.user_bio_data_collection.find_one({"user_id": id})
        if existing_user_bio_data is not None:
            return UserBioData(**existing_user_bio_data)
        raise DocumentNotFound()


    async def read_user_bio_data(self, user_id:ObjectId) -> UserBioData | None:
        """Read user data"""
        user_bio_data = await self.user_bio_data_collection.find_one({"user_id": user_id})
        if user_bio_data is None:
            return None
        return UserBioData(**user_bio_data)

    # User files data

    async def create_user_files(self, user_file :UserStaticFiles) -> ObjectId :
        result = await self.user_static_file_collection.insert_one(
            user_file.model_dump(by_alias=True)
        )
        return result.inserted_id

    async def update_user_files(self, user_id:ObjectId,user_file :UserStaticFiles) -> UserStaticFiles | None:
        """Update user static files data"""
        user_data = await self.user_static_file_collection.find_one({"_id": user_id})
        if user_data is None:
            raise DocumentNotFound()
        user_file_dict = {
            k: v for k, v in user_file.model_dump(by_alias=True).items() if v is not None
        }
        if len(user_file_dict) >= 1:
            update_result = await self.user_static_file_collection.find_one_and_update(
                {"user_id": user_id},
                {"$set": user_file_dict},
                return_document=ReturnDocument.AFTER,
            )
            if len(update_result) != 0:
                return UserStaticFiles(**update_result)
            else:
                raise DocumentNotFound()
        # The update is empty, but we should still return the matching document:
        existing_user_files_data = await self.user_static_file_collection.find_one({"user_id": id})
        if existing_user_files_data is not None:
            return UserStaticFiles(**existing_user_files_data)
        raise DocumentNotFound()



    async def read_user_files(self, user_id:ObjectId,) -> UserStaticFiles | None:
        user_files_data = await self.user_static_file_collection.find_one({"user_id": user_id})
        if user_files_data is None:
            return None
        return UserStaticFiles(**user_files_data)


    # Auth methods
    async def upsert_token(self, token: Token, user_id : ObjectId) -> Token:
        """Save a user token to the database."""
        result =  await self.auth_collection.find_one_and_update(
            filter={'user_id': user_id.__str__()},
            update={'$set' : token.model_dump(exclude={'id'}),},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return Token(**result)

        