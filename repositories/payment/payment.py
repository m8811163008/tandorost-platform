

from data.local_database import DatabaseInterface
from data.local_database.model.user_food_count import UserFoodCount
from data.local_database.model.user_subscription_payment_data import UserInDbSubscriptionPayment



class PaymentRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def create_payment_subscription(self, subscription_data: UserInDbSubscriptionPayment) ->UserInDbSubscriptionPayment:
        return await self.database.create_payment_subscription(subscription_data=subscription_data)

    
    async def read_payment_subscription(self, user_id :str )-> list[UserInDbSubscriptionPayment]:
        return await self.database.read_payment_subscription(user_id=user_id)
    
    async def read_user_food_count(self, user_id :str )-> UserFoodCount:
        return await self.database.read_user_food_counts(user_id=user_id)
