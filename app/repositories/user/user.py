

from datetime import datetime, timezone

from httpx import HTTPStatusError
from data.local_database import DatabaseInterface
from domain_models import  UserInDB, UserPhysicalDataUpsert, Referral,ReferralStatus, UsernameType,username_type, VerifyPhoneNumberDetail, RemoteApiInterface,NetworkConnectionError, EmailDetail,UserPhysicalData,SenderEmails, Role

class UserRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface, sms_body_id:str):
        self.database = database
        self.remote_api = remote_api
        self.sms_body_id = sms_body_id
    
    async def read_user(self, user_id : str) -> UserInDB | None:
        """Retrieve a user from the database."""
        return await self.database.read_user_by_id(
            user_id = user_id
        )
        
    async def read_user_count(self, roles : list[Role]) -> int | None:
        """Retrieve a user from the database."""
        return await self.database.read_user_count(role = roles)
    
    async def update_user(self, user : UserInDB)-> UserInDB | None:
        """Retrieve a user from the database."""
        assert(user.id is not None)
        return await self.database.upsert_user(
            user=user
        )
    
    async def read_user_physical_data(self, user_id:str) -> UserPhysicalData | None:
        return await self.database.read_user_physical_data(user_id = user_id)
    
    async def upsert_user_physical_data(self,user_id :str ,user_physical_data: UserPhysicalDataUpsert )-> UserPhysicalData:
        return await self.database.upsert_user_physical_data(user_physical_data=user_physical_data, user_id = user_id)
    

    async def delete_user_physical_data(self,user_id : str, data_point_id : str):
        await self.database.delete_user_physical_data(user_id = user_id, data_point_id=data_point_id)
        
    async def save_referral(self,inviter_id : str, invite_contact : str):
        referral = Referral(
            inviter_id = inviter_id,
            invited_contact = invite_contact,
            referral_value = "100",
            referral_benefit = r'100% discount for invited account',
            status = ReferralStatus.PENDING,
            created_at = datetime.now(timezone.utc),
            updated_at = datetime.now(timezone.utc)
        )
        await self.database.upsert_referral(referral=referral)
        
    async def read_referral_by_user_id(self, user_id: str) -> list[Referral]:
        return await self.database.read_referral_by_user_id(user_id=user_id)

    async def read_referral_by_inviter_id(self, inviter_id: str) -> list[Referral]:
        return await self.database.read_referral_by_inviter_id(inviter_id=inviter_id)
        

    async def update_referral_when_register(self,invite_contact : str, invited_user_id : str) -> list[Referral]:
        referrals = await self.database.read_referral_by_invite_contact(invite_contact=invite_contact)
        for referral in referrals:
            referral.updated_at = datetime.now(timezone.utc)
            referral.invited_user_id = invited_user_id
            referral.status = ReferralStatus.CLAIMED
            await self.database.upsert_referral(referral=referral)

    async def send_sms(self,inviter_id : str,phone_number : str):
        user_in_db = await self.database.read_user_by_id(user_id=inviter_id)
        try:
            detail = VerifyPhoneNumberDetail(text=[f"{user_in_db.full_name} مربی" if user_in_db.full_name is not None else "مربی"],to=phone_number, body_id=self.sms_body_id )
            await self.remote_api.send_sms_verification_code(detail=detail)
        except (HTTPStatusError, NetworkConnectionError, Exception):
            raise NetworkConnectionError()
    
    async def send_email(self,inviter_id : str, email : str,subject:str, body:str):
        user_in_db = await self.database.read_user_by_id(user_id=inviter_id)
        # update body
        coachname = f"{user_in_db.full_name} مربی" if user_in_db.full_name is not None else "مربی"
        body_with_code = body.format(code = coachname)
        
        try:
            detail = EmailDetail(sender_email = SenderEmails.verificationSender, recipient_email=email, subject=subject, body=body_with_code)
            await self.remote_api.send_email_verification_code(detail=detail)
        except Exception:
            raise NetworkConnectionError()