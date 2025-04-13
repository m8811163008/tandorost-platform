
from pydantic import BaseModel
from domain_models.data_models import Gender, BodyComposition



class UserBioDataRequest (BaseModel):
    gender : Gender
    age : int
    body_composition : BodyComposition
