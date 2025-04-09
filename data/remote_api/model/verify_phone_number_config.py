from pydantic import BaseModel, Field


class SMSPanelCongif(BaseModel):
    def __init__(self, username:str, password: str,) -> None:
        self.username = username
        self.password = password


class VerifyPhoneNumberDetail(BaseModel):
    def __init__(self,  text:list[str], to:str, body_id : str, ) -> None:
        self.text = text
        self.to = to
        self.body_id = Field( alias='bodyId', default=body_id)
        self.body_id = Field( body_id , alias='bodyId')
        self.uri = str

    