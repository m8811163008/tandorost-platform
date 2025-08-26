from abc import ABC, abstractmethod
import datetime

from data.local_database import Token


 
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
from data.local_database.model.user import UserInDB
from data.local_database.model.user_food_count import UserFoodCount
from data.local_database.model.user_physical_data import UserPhysicalData, UserPhysicalDataUpsert
from data.local_database.model.user_files import FileData, GallaryTag
from data.local_database.model.user_food import Food
from data.local_database.model.user_subscription_payment_data import UserInDbSubscriptionPayment


class DatabaseInterface(ABC):
    """
    DatabaseInterface is an abstract base class that defines the contract for interacting with a database. 
    It includes methods for managing users, user demographic data, user files, and authentication tokens.
    """
    # Clear the database , use with caution
    @abstractmethod
    async def clear(self):
        """For debugging. Use with caution."""
        pass

    @abstractmethod
    async def read_user_by_identifier(self, identifier: str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass
    

    @abstractmethod
    async def read_user_by_id(self, user_id : str) -> UserInDB | None:
        """Retrieve a user from the database."""
        pass

    # Users methods

    @abstractmethod
    async def upsert_user(self,user: UserInDB ) -> UserInDB:
        """Update a user in the database."""
        pass


    # User demographic data

    @abstractmethod
    async def upsert_user_physical_data(self,user_id : str, user_physical_data: UserPhysicalDataUpsert)-> UserPhysicalData:
        """Update user data"""
        pass

    @abstractmethod
    async def read_user_physical_data(self, user_id:str) -> UserPhysicalData | None:
        """Read user data"""
        pass

    @abstractmethod
    async def delete_user_physical_data(self,user_id : str, data_point_id : str):
        """Read user data"""
        pass


    # Auth methods
    @abstractmethod
    async def upsert_token(self,  token: Token) -> Token:
        """Save a user token to the database."""
        pass
    
    @abstractmethod
    async def delete_token(self,  user_id: str) -> None:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def read_token(self,  user_id:str) -> Token | None:
        """Save a user token to the database."""
        pass

    # User statics files

    @abstractmethod
    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def read_user_static_files(self,  user_id:str) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def upsert_user_files(self,  user_files:list[FileData]) -> list[FileData]:
        """Save a user token to the database."""
        pass

    @abstractmethod
    async def archive_images(self, images_id : list[str]) -> list[str] :
        """Save a user token to the database."""
        pass


    # User food nutritions
    @abstractmethod
    async def read_user_foods(self,  user_id:str, start_date: datetime.datetime, end_date: datetime.datetime) -> list[Food]:
        pass

    @abstractmethod
    async def upsert_user_foods(self, user_foods: list[Food]) -> list[Food]:
        pass

    @abstractmethod
    async def delete_user_foods(self,  foods_ids: list[str]) -> list[str]:
        pass

    @abstractmethod
    async def create_payment_subscription(self, subscription_data: UserInDbSubscriptionPayment) ->UserInDbSubscriptionPayment:
        pass

    @abstractmethod
    async def read_payment_subscription(self, user_id :str )-> list[UserInDbSubscriptionPayment]:
        pass
    
    @abstractmethod
    async def update_payment_subscription(self, payment_subscription :UserInDbSubscriptionPayment)-> UserInDbSubscriptionPayment:
        pass

    @abstractmethod
    async def read_user_food_counts(self, user_id :str )-> UserFoodCount:
        pass
    
    @abstractmethod
    async def upsert_coach(self, coach :Coach )-> Coach:
        pass
    
    @abstractmethod
    async def read_coach(self, user_id :str )-> Coach:
        pass
    
    @abstractmethod
    async def upsert_coach_program(self, program :CoachProgram )-> CoachProgram:
        pass
    
    @abstractmethod
    async def delete_coach_program(self, program_id :str )-> None:
        pass
    
    @abstractmethod
    async def read_coach_programs(self, user_id :str )-> list[CoachProgram]:
        pass