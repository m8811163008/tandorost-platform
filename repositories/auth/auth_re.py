
from datetime import datetime, timedelta
from random import Random

from data.local_database import DatabaseInterface, Token
from data.remote_api import VerifyPhoneNumberDetail, RemoteApiInterface
from data.remote_api.model.email_config import EmailDetail, SenderEmails
from domain_models import InvalidPassword, UsernameAlreadyInUse, UsernameIsInactive, UsernameNotRegisteredYet, InvalidVerificationCode, NetworkConnectionError, HTTPStatusError,VerificationCode,VerificationType, UserInDB
from repositories.auth.utility import UsernameType, create_access_token, get_password_hash,is_valid_password, username_type
from utility.envirement_variables import EnvirenmentVariable



class AuthRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface, sms_body_id:str):
        self.database = database
        self.remote_api = remote_api
        self.sms_body_id = sms_body_id

    #TODO user name is phone number , in future change to use both email and phone number
    async def save_verification_code(self, identifier : str,  verification_type: VerificationType):
        user_in_db = await self.database.read_user_by_identifier(identifier=identifier)
        
        if user_in_db is None and verification_type.is_forgot_password():
            raise UsernameNotRegisteredYet()
        
        user_type = username_type(username=identifier)
        if user_in_db is not None and verification_type.is_register():
            
            if user_type == UsernameType.PHONENUMBER and user_in_db.is_phone_number_verified:
                raise UsernameAlreadyInUse()
            if user_type == UsernameType.EMAIL and user_in_db.is_email_verified:
                raise UsernameAlreadyInUse()
        
        user_id =  None
        if user_in_db is not None and user_in_db.id is not None:
            user_id = user_in_db.id
        current_phone_number_verification_code = None if user_in_db is None else user_in_db.verification_code.phone_number_verification_code
        current_email_verification_code =  None if user_in_db is None else user_in_db.verification_code.email_verification_code
        random_code = str(Random().randint(1000, 9999))
        verification_code = VerificationCode(created_at= datetime.now().isoformat(),
                                             phone_number_verification_code=random_code if user_type == UsernameType.PHONENUMBER else current_phone_number_verification_code,
                                             email_verification_code=random_code if user_type == UsernameType.EMAIL else current_email_verification_code,)
        current_user_phone_number =  None if user_in_db is None else user_in_db.phone_number
        current_user_email =  None if user_in_db is None else user_in_db.email
    
        user = UserInDB(_id = user_id ,
                        phone_number = identifier if user_type == UsernameType.PHONENUMBER else current_user_phone_number,
                        email = identifier if user_type == UsernameType.EMAIL else current_user_email,
                        verification_code=verification_code)
        
        await self.database.upsert_user(user=user)
        

            
    async def send_sms_verification_code(self,username : str,):
        user_in_db = await self.database.read_user_by_identifier(identifier=username)
        try:
            detail = VerifyPhoneNumberDetail(text=[user_in_db.verification_code.phone_number_verification_code],to=username, body_id=self.sms_body_id )
            await self.remote_api.send_sms_verification_code(detail=detail)
        except (HTTPStatusError, NetworkConnectionError, Exception):
            raise NetworkConnectionError()
    
    async def send_email_verification_code(self,username : str,subject:str, body:str):
        user_in_db = await self.database.read_user_by_identifier(identifier=username)
        # update body
        body_with_code = body.format(code = user_in_db.verification_code.email_verification_code)
        
        try:
            detail = EmailDetail(sender_email = SenderEmails.verificationSender, recipient_email=username, subject=subject, body=body_with_code)
            await self.remote_api.send_email_verification_code(detail=detail)
        except Exception:
            raise NetworkConnectionError()
    
    async def verify_code(self, username:str, verification_code : str, is_register_request : bool = True):
        user = await self.database.read_user_by_phone_number(phone_number=username)
        if user is None :
            raise UsernameNotRegisteredYet()
        if user.verification_code is None:
            raise UsernameNotRegisteredYet()
        if user.verification_code.verification_code != verification_code:
            raise InvalidVerificationCode()
        if user.is_phone_number_verified and is_register_request:
            raise UsernameAlreadyInUse()

    async def update_user_account(self, password: str, username:str, is_verified : bool = True) -> UserInDB:
        user = await self.database.read_user_by_phone_number(phone_number=username)
        assert(user is not None)
        hashed_password = get_password_hash(password=password)
        user.hashed_password = hashed_password
        user.is_phone_number_verified = is_verified
        assert(user.id is not None)
        return await self.database.upsert_user(user=user)

    async def authenticate(self,username: str, password: str) :
        user = await self.database.read_user_by_phone_number(username)
        if user is None or user.hashed_password is None:
            raise UsernameNotRegisteredYet()
        if user.is_phone_number_verified is False:
            raise UsernameIsInactive()
        if is_valid_password(password, user.hashed_password) is False:
            raise InvalidPassword()
    
    async def issue_access_token(self,username: str, access_token_expire_minute: float) -> Token:
        # Todo implement refresh token
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
    
    async def read_user_by_identifier(self, identifier: str):
        return await self.database.read_user_by_identifier(identifier=identifier)
        
        