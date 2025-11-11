from pydantic import BaseModel, Field


class SMSPanelCongif(BaseModel):
    username: str
    password :str



class VerifyPhoneNumberDetail(BaseModel):
    text : list[str]
    to : str
    bodyId : str = Field(alias='body_id')


    