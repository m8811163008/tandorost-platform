from abc import ABC, abstractmethod

from pydantic import UUID4
from data.local_database import Token

from data.local_database.model.user import UserInDB
from data.local_database.model.user_bio_data import UserBioData
from data.local_database.model.user_files import UserStaticFiles


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

    @abstractmethod
    async def read_user_by_id(self, user_id : UUID4) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    # Users methods

    @abstractmethod
    async def upsert_user(self,user: UserInDB, id: UUID4 | None = None ) -> UserInDB:
        """Update a user in the database."""
        pass


    # User demographic data

    @abstractmethod
    async def upsert_user_bio_data(self, user_id : UUID4, user_bio_data: UserBioData)-> UserBioData:
        """Update user data"""
        pass

    @abstractmethod
    async def read_user_bio_data(self, user_id:UUID4) -> UserBioData | None:
        """Read user data"""
        pass


    @abstractmethod
    async def upsert_user_files(self, user_id:UUID4,user_file :UserStaticFiles) -> UserStaticFiles | None:
        pass


    @abstractmethod
    async def read_user_files(self, user_id:UUID4,) -> UserStaticFiles | None:
        pass


    # Auth methods
    @abstractmethod
    async def upsert_token(self, user_id: UUID4, token: Token) -> Token:
        """Save a user token to the database."""
        pass

