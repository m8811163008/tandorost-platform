
from datetime import timedelta
from uuid import UUID

from data.local_database import DatabaseInterface, Token
from data.remote_api import VerifyPhoneNumberDetail, RemoteApiInterface
from domain_models import InvalidPassword, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, InvalidVerificationCode, NetworkConnectionError, HTTPStatusError,VerificationCode,VerificationType, UserInDB
from repositories.auth.utility import create_access_token, get_password_hash,is_valid_password
from utility.envirement_variables import EnvirenmentVariable


class AuthRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api


    async def get_token(self, id: UUID) -> Token | None:
        return await self.database.get_token(id=id)
    
    async def send_verification_code(self, code: VerificationCode, username : str, body_id : str, verification_type: VerificationType   ):
        try:
            await self._upsert_user(code= code, username = username, verification_type = verification_type)
            detail = VerifyPhoneNumberDetail(text=[code.verification_code],to=username, body_id=body_id )
            await self.remote_api.send_verification_code(detail=detail)
        except UsernameAlreadyInUse as e:
            raise e
        except (HTTPStatusError, NetworkConnectionError, Exception):
            raise NetworkConnectionError()
    
    async def verify_code(self, username:str, verification_code : str):
        user = await self.database.read_user(username=username)
        if user is None :
            raise UsernameNotRegisteredYet()
        if user.verification_code is None:
            raise UsernameNotRegisteredYet()
        if user.verification_code.verification_code != verification_code:
            raise InvalidVerificationCode()

    

    async def update_user_account(self, password: str, username:str, is_enabled : bool | None = None) -> UserInDB:
        user = await self.database.read_user(username=username)
        assert(user is not None)
        hashed_password = get_password_hash(password=password)
        user.hashed_password = hashed_password
        if is_enabled is not None:
            user.is_verified = is_enabled
        assert(user.id is not None)
        return await self.database.update_user(id = user.id, user=user)
    

    async def authenticate(self,username: str, password: str) :
        user = await self.database.read_user(username)
        if user is None or user.hashed_password is None:
            raise UsernameNotRegisteredYet()
        if user.is_verified is False:
            raise UsernameIsInactive()
        if is_valid_password(password, user.hashed_password) is False:
            raise InvalidPassword()
    
    async def issue_access_token(self,username: str, access_token_expire_minute: float) -> Token:
        user = await self.database.read_user(username)
        assert(user is not None and user.id is not None)
        access_token_expires = timedelta(minutes=access_token_expire_minute)
        access_token = create_access_token(
            data={"sub": username,
                  "user_id" : user.id.__str__()}, 
            key = EnvirenmentVariable.SECRET_KEY(),
            algorithm= EnvirenmentVariable.ALGORITHM(),
            expires_delta=access_token_expires
        )
        token_instance = Token(access_token=access_token, token_type="bearer", user_id= user.id)
        return await self.database.save_token(token=token_instance, user_id=user.id)
        
        
    async def _upsert_user(self, code: VerificationCode, username : str, verification_type: VerificationType):
        user = await self.database.read_user(username=username)
        if user is None:
            user = UserInDB(phone_number=username, verification_code=code)
            await self.database.create_user(user=user)
        else :
            if user.is_verified and verification_type.is_register() :
                raise UsernameAlreadyInUse() 
            user.verification_code = code
            assert(user.id is not None)
            await self.database.update_user(id = user.id, user=user)