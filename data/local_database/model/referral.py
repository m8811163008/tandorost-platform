from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Literal, Optional


class ReferralStatus(StrEnum):
    PENDING = 'pending' 
    CLAIMED = 'claimed'  
    EXPIRED = 'expired'
    
class Referral(BaseModel):
    """
    Model representing the full referral document stored in the database.
    """
    id : str | None = Field(alias="_id", default=None)
    inviter_id: str
    invited_contact: str
    referral_value: str | None = None
    referral_benefit: str | None 
    
    # Status tracking for claiming the benefit
    status: ReferralStatus | None = None
    invited_user_id: str | None = None
    
    # Timestamps
    created_at: datetime 
    updated_at: datetime 
    model_config = ConfigDict(
        use_enum_values=True,
        populate_by_name=True,
    )