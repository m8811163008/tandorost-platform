from abc import ABC, abstractmethod
from domain_models.user import UserInDB
from data.local_database.model.token import Token
from uuid import UUID


class DatabaseInterface(ABC):
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

    #Auth methods
    @abstractmethod
    async def save_token(self, token: Token) -> Token:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def get_token(self, id: UUID) -> Token | None:
        """Retrieve a user token from the database."""
        pass