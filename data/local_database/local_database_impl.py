
from uuid import uuid4
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
from data.local_database.model.user_files import UserStaticFiles, GallaryTag, FileMetaData



class LocalDataBaseImpl(DatabaseInterface):
    def __init__(self, uri: str, database_name: str):
        self.client: AsyncIOMotorClient[dict[str,Any]] = AsyncIOMotorClient(uri)
        self.db :AsyncIOMotorDatabase[dict[str,Any]] = self.client[database_name]
        self.user_collection : AsyncIOMotorCollection[dict[str,Any]] = self.db["UserCollection"]
        self.auth_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["TokenCollection"]
        self.user_bio_data_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserBioDataCollection"]
        self.user_static_file_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserStaticsFileCollection"]


    async def clear(self):
        await self.user_collection.delete_many({})
        await self.auth_collection.delete_many({})
        await self.user_bio_data_collection.delete_many({})
        await self.user_static_file_collection.delete_many({})
        print('*****Database cleared!*****')
    


    async def _raise_for_invalid_user(self, user_id: str):
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            raise DocumentNotFound()

    async def read_user_by_phone_number(self, phone_number:str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"phone_number": phone_number})
        if user_data is None:
            return None
        return UserInDB(**user_data)
     
    async def read_user_by_id(self, user_id : str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            return None
        return UserInDB(**user_data)
    
    async def upsert_user(self, user: UserInDB)-> UserInDB:
        if user.id is None:
            user.id = str(uuid4())
        update_result = await self.user_collection.find_one_and_update(
            filter={"_id": user.id},
            update={"$set": user.model_dump(by_alias=True,exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )
        return UserInDB(**update_result)
        
    async def read_user_bio_data(self, user_id:str) -> UserBioData | None:
        """Read user data"""
        user_bio_data = await self.user_bio_data_collection.find_one({"user_id": user_id})
        if user_bio_data is None:
            return None
        return UserBioData(**user_bio_data)

    async def upsert_user_bio_data(self, user_bio_data: UserBioData)-> UserBioData:
        """Update user data"""
        if user_bio_data.id is None:
            user_bio_data.id = str(uuid4())
        # TODO TEST lists
        await self._raise_for_invalid_user(user_id = user_bio_data.user_id)
        update_result = await self.user_bio_data_collection.find_one_and_update(
                filter={"user_id": user_bio_data.user_id},
                update={"$set": user_bio_data.model_dump(exclude_none=True, by_alias=True)},
                return_document=ReturnDocument.AFTER,
                upsert=True
            )
        return UserBioData(**update_result)

    # User files data
    
    async def read_user_image_gallary(self,  user_id:str, tags:list[str | GallaryTag]) -> dict[str | GallaryTag, list[FileMetaData]] | None:
        """Save a user token to the database."""
        files_dict = await self.user_static_file_collection.find_one({'user_id':user_id})
        if files_dict is None:
            return None
        files = UserStaticFiles(**files_dict)
        result : dict[str | GallaryTag, list[FileMetaData]] = {}
        for tag in tags:
            tag_key = tag.value if isinstance(tag, GallaryTag) else tag  # Convert GallaryTag to its key representation
            if tag_key in files.image_gallery:
                result[tag_key] = files.image_gallery[tag_key]
        return result

    
    async def read_user_static_files(self,  user_id:str) -> UserStaticFiles | None:
        """Save a user token to the database."""
        files_dict = await self.user_static_file_collection.find_one({'user_id':user_id})
        if files_dict is None :
            return None
        return UserStaticFiles(**files_dict)
    
    
    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        """Save a user token to the database."""
        if user_files.id is None:
            user_files.id = str(uuid4())
        # TODO TEST lists
        await self._raise_for_invalid_user(user_id = user_files.user_id)
        update_result = await self.user_bio_data_collection.find_one_and_update(
                filter={"user_id": user_files.user_id},
                update={"$set": user_files.model_dump(exclude_none=True, by_alias=True)},
                return_document=ReturnDocument.AFTER,
                upsert=True
            )
        return UserStaticFiles(**update_result)


    # Auth methods
    async def upsert_token(self, token: Token) -> Token:
        """Save a user token to the database."""
        if token.id is None:
            token.id = str(uuid4())
        result =  await self.auth_collection.find_one_and_update(
            filter={'user_id': token.user_id},
            update={'$set' : token.model_dump(by_alias=True, exclude_none=True),},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return Token(**result)
    

    async def read_token(self,  user_id:str) -> Token | None:
        """Save a user token to the database."""
        token = await self.auth_collection.find_one({'user_id' : user_id})
        if token is None:
            return None
        return Token(**token)