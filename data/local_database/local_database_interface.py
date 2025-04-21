from abc import ABC, abstractmethod
import datetime

from data.local_database import Token


from data.local_database.model.user import UserInDB
from data.local_database.model.user_bio_data import UserBioData
from data.local_database.model.user_files import FileMetaData, GallaryTag, UserStaticFiles
from data.local_database.model.user_food import UserFood


class DatabaseInterface(ABC):
    """
    DatabaseInterface is an abstract base class that defines the contract for interacting with a database. 
    It includes methods for managing users, user demographic data, user files, and authentication tokens.
    """
    # Clear the database , use with caution
    @abstractmethod
    async def clear(self):
        """For debugging. Use with caution."""
        pass

    @abstractmethod
    async def read_user_by_phone_number(self, phone_number: str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    @abstractmethod
    async def read_user_by_id(self, user_id : str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    # Users methods

    @abstractmethod
    async def upsert_user(self,user: UserInDB ) -> UserInDB:
        """Update a user in the database."""
        pass


    # User demographic data

    @abstractmethod
    async def upsert_user_bio_data(self, user_bio_data: UserBioData)-> UserBioData:
        """Update user data"""
        pass

    @abstractmethod
    async def read_user_bio_data(self, user_id:str) -> UserBioData | None:
        """Read user data"""
        pass


    # Auth methods
    @abstractmethod
    async def upsert_token(self,  token: Token) -> Token:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def read_token(self,  user_id:str) -> Token | None:
        """Save a user token to the database."""
        pass

    # User statics files

    @abstractmethod
    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> dict[GallaryTag, list[FileMetaData]] | None:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def read_user_static_files(self,  user_id:str) -> UserStaticFiles | None:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def archive_images(self,user_id:str, images_id : list[str]) -> list[str] | None:
        """Save a user token to the database."""
        pass


    # User food nutritions
    @abstractmethod
    async def read_user_foods(self,  user_id:str, start_date: datetime.datetime, end_date: datetime.datetime) -> UserFood | None:
        pass

    @abstractmethod
    async def upsert_user_foods(self, user_food:UserFood) -> UserFood:
        pass

    @abstractmethod
    async def delete_user_foods(self,  user_id:str, foods_ids: list[str]) -> list[str] | None:
        pass

