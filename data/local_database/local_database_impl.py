
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
from data.local_database.model.user_files import (
    UserStaticFiles, 
    GallaryTag, 
    FileMetaData, 
    ProcessingStatus
    )



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
    
    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> dict[GallaryTag, list[FileMetaData]] | None:
        """Retrieve user image gallery based on tags."""
        # await self.user_static_file_collection.delete_many({})
        files_dict = await self.user_static_file_collection.find_one({'user_id':user_id})
        if files_dict is None:
            return None
        
        files = UserStaticFiles(**files_dict)
        result : dict[GallaryTag, list[FileMetaData]] = {}

        for tag in tags:
            # Check if the tag exists in the image_gallery dictionary
            if tag in files.image_gallery:
                result[tag] = files.image_gallery[tag]

        return result

    
    async def read_user_static_files(self,  user_id:str) -> UserStaticFiles | None:
        """Save a user token to the database."""
        
        files_dict = await self.user_static_file_collection.find_one({'user_id':user_id})
        if files_dict is None :
            return None
        return UserStaticFiles(**files_dict)
    
    
    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        """Save a user token to the database."""
        user_files_db = await self.read_user_static_files(user_id = user_files.user_id)
        if user_files_db is not None:
            user_files.id = user_files_db.id
        else:
            user_files_db = UserStaticFiles(user_id=user_files.user_id, image_gallery={})
            user_files.id = user_files_db.id = str(uuid4())

        # Ensure the user exists
        await self._raise_for_invalid_user(user_id = user_files.user_id)

        # merge user_files_db and user_files
        update_tag = user_files.image_gallery.keys()
        assert(len(update_tag) == 1)
        tag = next(iter(update_tag))  # Retrieve the single tag from the keys
        if tag not in user_files_db.image_gallery:
            user_files_db.image_gallery[tag] = []
        user_files_db.image_gallery[tag].extend(user_files.image_gallery[tag])

        # Convert enum keys in `image_gallery` to strings
        user_files_dict = user_files_db.model_dump(exclude_none=True, by_alias=True)

        await self.user_static_file_collection.find_one_and_update(
                filter={"user_id": user_files.user_id},
                update={"$set": user_files_dict},
                return_document=ReturnDocument.AFTER,
                upsert=True
            )
        return user_files
    
    
    async def archive_images(self,user_id:str, images_id : list[str] ) -> list[str] | None:
        """archive user images."""
        user_files_db = await self.read_user_static_files(user_id = user_id)
        if user_files_db is None:
            return None
        # Ensure the user exists
        await self._raise_for_invalid_user(user_id = user_id)
        updated_image_ids:list[str] = []
        for db_images in user_files_db.image_gallery.values():
            for db_image in db_images:
                for image_id in images_id:
                    if db_image.image_id == image_id:
                        updated_image_ids.append(image_id)
                        db_image.processing_status = ProcessingStatus.ARCHIVED
        
        return updated_image_ids


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
    