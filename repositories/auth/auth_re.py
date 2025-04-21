
from datetime import timedelta

from data.local_database import DatabaseInterface, Token
from data.remote_api import VerifyPhoneNumberDetail, RemoteApiInterface
from domain_models import InvalidPassword, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, InvalidVerificationCode, NetworkConnectionError, HTTPStatusError,VerificationCode,VerificationType, UserInDB
from repositories.auth.utility import create_access_token, get_password_hash,is_valid_password
from utility.envirement_variables import EnvirenmentVariable



class AuthRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api

    #TODO user name is phone number , in future change to use both email and phone number
    async def send_verification_code(self, code: VerificationCode, username : str, body_id : str, verification_type: VerificationType):
        user_in_db = await self.database.read_user_by_phone_number(phone_number=username)
        if user_in_db is None and verification_type.is_forgot_password():
            raise UsernameNotRegisteredYet()
        if user_in_db is not None and user_in_db.is_verified and verification_type.is_register():
            raise UsernameAlreadyInUse()
        
        user_id =  None
        if user_in_db is not None and user_in_db.id is not None:
            user_id = user_in_db.id
    
        user = UserInDB(_id = user_id , phone_number=username, verification_code=code)
        await self.database.upsert_user(user=user)
            
        try:
            detail = VerifyPhoneNumberDetail(text=[code.verification_code],to=username, body_id=body_id )
            await self.remote_api.send_verification_code(detail=detail)
        except (HTTPStatusError, NetworkConnectionError, Exception):
            raise NetworkConnectionError()
    
    async def verify_code(self, username:str, verification_code : str):
        user = await self.database.read_user_by_phone_number(phone_number=username)
        if user is None :
            raise UsernameNotRegisteredYet()
        if user.verification_code is None:
            raise UsernameNotRegisteredYet()
        if user.verification_code.verification_code != verification_code:
            raise InvalidVerificationCode()

    async def update_user_account(self, password: str, username:str, is_verified : bool = True) -> UserInDB:
        user = await self.database.read_user_by_phone_number(phone_number=username)
        assert(user is not None)
        hashed_password = get_password_hash(password=password)
        user.hashed_password = hashed_password
        user.is_verified = is_verified
        assert(user.id is not None)
        return await self.database.upsert_user(user=user)

    async def authenticate(self,username: str, password: str) :
        user = await self.database.read_user_by_phone_number(username)
        if user is None or user.hashed_password is None:
            raise UsernameNotRegisteredYet()
        if user.is_verified is False:
            raise UsernameIsInactive()
        if is_valid_password(password, user.hashed_password) is False:
            raise InvalidPassword()
    
    async def issue_access_token(self,username: str, access_token_expire_minute: float) -> Token:
        user = await self.database.read_user_by_phone_number(username)
        assert(user is not None and user.id is not None)
        access_token_expires = timedelta(minutes=access_token_expire_minute)
        access_token = create_access_token(
            data={"sub": username,
                  "user_id" : user.id.__str__()}, 
            key = EnvirenmentVariable.SECRET_KEY(),
            algorithm= EnvirenmentVariable.ALGORITHM(),
            expires_delta=access_token_expires
        )
        token_instance = Token(user_id= user.id,access_token=access_token, token_type="bearer")
        tokne_in_db = await self.database.read_token(user_id = user.id)
        if tokne_in_db is not None:
            token_instance.id = tokne_in_db.id
        return await self.database.upsert_token(token = token_instance)
    
    async def read_user_by_phone_number(self, username: str):
        return await self.database.read_user_by_phone_number(phone_number=username)
        