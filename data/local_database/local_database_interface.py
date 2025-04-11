from abc import ABC, abstractmethod

from bson import ObjectId
from domain_models import UserInDB
from data.local_database import Token
from uuid import UUID


class DatabaseInterface(ABC):
    # Clear the database , use with caution
    @abstractmethod
    async def clear(self):
        """For debugging. Use with caution."""
        pass

    # Users methods
    @abstractmethod
    async def create_user(self, user: UserInDB) -> str:
        """Save a user to the database."""
        pass

    @abstractmethod
    async def update_user(self, id: str, user: UserInDB) -> UserInDB:
        """Update a user in the database."""
        pass

    @abstractmethod
    async def read_user(self, username: str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    # User demographic data
    @abstractmethod
    async def read_user_bio_data(self, user_id:ObjectId):
        """For debugging. Use with caution."""
        pass

    # User demographic data
    @abstractmethod
    async def read_user_files(self, user_id:ObjectId, ):
        """For debugging. Use with caution."""
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