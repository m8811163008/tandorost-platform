from uuid import UUID

from data.local_database.local_database_interface import DatabaseInterface
from data.remote_api.model.verify_phone_number_config import VerifyPhoneNumberDetail
from data.local_database.model.token import Token
from domain_models.exceptions import NetworkConnectionError
from domain_models.data_models import HTTPStatusError

from data.remote_api.remote_api_interface import RemoteApiInterface


class AuthRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api

    async def save_token(self, token: Token) -> Token:
        return await self.database.save_token(token=token)


    async def get_token(self, id: UUID) -> Token | None:
        return await self.database.get_token(id=id)
    
    async def send_verification_code(self, code: str, to : str, body_id : str):
        try:
            detail = VerifyPhoneNumberDetail(text=[],to='', body_id='12' )
            await self.remote_api.verify_phone_number(detail=detail)
        except HTTPStatusError:
            raise NetworkConnectionError()