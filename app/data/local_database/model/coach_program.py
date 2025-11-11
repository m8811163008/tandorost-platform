
from enum import StrEnum
from pydantic import  BaseModel, Field,ConfigDict

from .currency import Currency

class ProgramFeature(StrEnum):
    PHONE_SUPPORT = 'phone_support'
    PERSONALIZED_NUTRITION_GUIDE = 'personalized_nutrition_guide'
    PERSONALIZED_SPORT_SUPPLEMENT_GUIDE = 'personalized_sport_supplement_guide'
    FORMING_CHECK_VIDEO_SUPPORT = 'forming_check_video_support'

    
class CoachProgram(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    title : str
    description : str
    duration_weeks: int
    price : float
    currency : Currency
    features : list[ProgramFeature] = []
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


        
    