from abc import ABC, abstractmethod
import datetime

from data.local_database import Token


from data.local_database.model.user import UserInDB
from data.local_database.model.user_bio_data import UserBioData, UserBioDataUpsert
from data.local_database.model.user_files import FileData, GallaryTag
from data.local_database.model.user_food import Food


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
    async def upsert_user_bio_data(self,user_id : str, user_bio_data: UserBioDataUpsert)-> UserBioData:
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
    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def read_user_static_files(self,  user_id:str) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def upsert_user_files(self,  user_files:list[FileData]) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def archive_images(self, images_id : list[str]) -> list[str] :
        """Save a user token to the database."""
        pass


    # User food nutritions
    @abstractmethod
    async def read_user_foods(self,  user_id:str, start_date: datetime.datetime, end_date: datetime.datetime) -> list[Food]:
        pass

    @abstractmethod
    async def upsert_user_foods(self, user_foods: list[Food]) -> list[Food]:
        pass

    @abstractmethod
    async def delete_user_foods(self,  foods_ids: list[str]) -> list[str]:
        pass

