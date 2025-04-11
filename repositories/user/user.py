

from data.local_database import DatabaseInterface
from domain_models import UsernameAlreadyInUse, UserInDB

class UserRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    async def create_user(self, user: UserInDB) -> str:
        """Save a user token to the database."""
        current_user = await self.database.read_user(
            username= user.phone_number 
        )
        if current_user is not None and current_user.is_enabled:
            raise UsernameAlreadyInUse()
        return await self.database.create_user(user=user)
    

    async def get_user(self, user_name: str) -> UserInDB | None:
        """Retrieve a user from the database."""
        return await self.database.read_user(
            username= user_name 
        )