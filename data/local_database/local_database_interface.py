from abc import ABC, abstractmethod

from domain_models import UserInDB
from data.local_database import Token
from uuid import UUID

from domain_models.pydantic_object_id import ObjectId
from domain_models.user_bio_data import UserBioData
from domain_models.user_files import UserStaticFiles


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
    async def read_user(self, username: str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    # Users methods
    @abstractmethod
    async def create_user(self, user: UserInDB) -> ObjectId:
        """Save a user to the database."""
        pass

    @abstractmethod
    async def update_user(self, id: str, user: UserInDB) -> UserInDB:
        """Update a user in the database."""
        pass


    # User demographic data
    @abstractmethod
    async def create_user_bio_data(self, user_bio_data: UserBioData)-> ObjectId:
        """Create user data and return its assigned ID"""
        pass

    @abstractmethod
    async def update_user_bio_data(self, user_id : ObjectId, user_bio_data: UserBioData)-> UserBioData:
        """Update user data"""
        pass

    @abstractmethod
    async def read_user_bio_data(self, user_id:ObjectId) -> UserBioData | None:
        """Read user data"""
        pass

    # User files data
    """
    Abstract method to create user files in the local database.

    Args:
        user_file (UserStaticFiles): An instance of UserStaticFiles containing
                                     the details of the user file to be created.

    Returns:
        str: A string representing the identifier or path of the created user file.

    Raises:
        NotImplementedError: This method must be implemented in a subclass.
    """
    @abstractmethod
    async def create_user_files(self, user_file :UserStaticFiles) -> ObjectId :
        pass

    @abstractmethod
    async def update_user_files(self, user_id:ObjectId,user_file :UserStaticFiles) -> UserStaticFiles | None:
        pass


    @abstractmethod
    async def read_user_files(self, user_id:ObjectId,) -> UserStaticFiles | None:
        pass


    # Auth methods
    @abstractmethod
    async def save_token(self, token: Token, user_id: ObjectId) -> Token:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def get_token(self, id: UUID) -> Token | None:
        """Retrieve a user token from the database."""
        pass