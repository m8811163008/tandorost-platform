from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient
from domain_models.token import Token
from typing import Any

class TokenRepository:
    def __init__(self, uri: str, database_name: str):
        self.client: Any = AsyncIOMotorClient(uri)
        self.db = self.client[database_name]
        self.collection = self.db["tokens"]

    async def save_token(self, token: Token) -> Token:
        """Save a user token to the database."""
        token_id = await self.collection.insert_one(
            token.model_dump(by_alias=True, exclude={"id"})
        )
        saved_token = await self.collection.find_one(
            {"_id": token_id}
        )
        return saved_token


    async def get_token(self, id: UUID) -> Token | None:
        """Retrieve a user token from the database."""
        token_data = await self.collection.find_one({"_id": id})
        if token_data:
            return Token(**token_data)
        return None