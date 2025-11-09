
from datetime import datetime, timezone
from enum import StrEnum
from pydantic import   BaseModel, Field, ConfigDict, computed_field

from .currency import Currency


class PaymentMethod(StrEnum):
    INPAYMENTCAFEBAZZAR = 'in_app_payment_cafe_bazzar'
    TANDOROSTWEBSITE = 'tandorost_website'

class SubscriptionType(StrEnum):
    FREETIER = 'free_tier'
    ONEMONTH = 'one_month'
    THREEMONTH = 'three_month'
    SIXMONTH = 'six_month'

class PaymentStatus(StrEnum):
    PENDING_SETTLE = 'pending_settle'
    PENDING_TRANSFER = 'pending_transfer'
    FAILED = 'failed'
    COMPLETED = 'completed'
    REFUND = 'refund'
    


class UserInDbSubscriptionPayment(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    subscriber_user_id : str
    coach_user_id : str | None = None
    program_id : str | None = None
    cafe_bazzar_order_id : str | None = None
    payment_status : PaymentStatus = PaymentStatus.PENDING_SETTLE
    platform_settlement_month: datetime | None = None
    paid_amount: float
    discount_amount : float
    currency: Currency
    payment_method: PaymentMethod
    purchase_date: datetime
    subscription_type: SubscriptionType
    updated_at: datetime | None = None
    user_ai_requested_foods : int = 0
    

    
    model_config = ConfigDict(use_enum_values=True, populate_by_name=True)


    @computed_field
    @property
    def user_ai_request_limit_foods(self) -> int:
        # For Gemini: 1 voice request per food, assume 10 foods for free tier
        if self.subscription_type == SubscriptionType.FREETIER:
            return 3
        # For ONEMONTH: 20 requests per day, assume 30 days in a month
        elif self.subscription_type == SubscriptionType.ONEMONTH:
            return 20 * 30
        # For THREEMONTH: 20 requests per day, 90 days
        elif self.subscription_type == SubscriptionType.THREEMONTH:
            return 20 * 90
        elif self.subscription_type == SubscriptionType.SIXMONTH:
            return 20 * 180
        else:
            return 0
    
    @computed_field
    @property
    def is_active(self) -> bool:
        # TODO add expiry date when program_id is not null
        now = datetime.now(timezone.utc)
        expiry = self.purchase_date.replace(tzinfo=timezone.utc)
        if self.subscription_type == SubscriptionType.ONEMONTH:
            
            if (now - expiry).days >= 30:
                return False
        elif self.subscription_type == SubscriptionType.THREEMONTH:

            if (now - expiry).days >= 90:
                return False
        elif self.subscription_type == SubscriptionType.SIXMONTH:
            #expiry = self.purchase_date.replace(tzinfo=timezone.utc) if self.purchase_date.tzinfo else self.purchase_date
            if (now - expiry).days >= 180:
                return False

        return self.user_ai_requested_foods < self.user_ai_request_limit_foods
