from enum import StrEnum
from pydantic import BaseModel, Field


class EmailSMTPCongif(BaseModel):
    username: str
    appPassword :str
    host: str
    port: int



class EmailDetail(BaseModel):
    sender_email: str
    recipient_email: str
    subject: str
    body: str

class SenderEmails(StrEnum):
    verificationSender : str = ''