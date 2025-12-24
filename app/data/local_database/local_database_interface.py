from abc import ABC, abstractmethod
import datetime
from typing import Tuple

from .model import( Token, Coach, CoachProgram,DocumentNotFound, UserPhysicalDataValidationError,ExercisesDefinition,
                    ExerciseDefinition,
                    Role,
                    TraineeHistory,
                    UserInDB,
                    UserFoodCount,
                    DataPoint, UserPhysicalData, UserPhysicalDataUpsert,
                    GallaryTag, 
                    FileData, 
                    ProcessingStatus,
                    Food,
                    UserInDbSubscriptionPayment,
                    ProgramEnrollment,
                    WorkoutProgram,
                    Referral,
                    PaymentStatus
                   )





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
    async def save_najva_sms_to_local(self, numbers : list[str],) -> Tuple[list[str], int]:
        # return last index of saved number and non duplicated numbers
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
    async def read_payment_subscription_by_coach_user_id(self, coach_id :str )-> list[UserInDbSubscriptionPayment]:
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
    
    @abstractmethod
    async def read_coaches(self)-> list[Coach]:
        pass
    
    @abstractmethod
    async def read_coaches_profile(self)-> list[UserInDB]:
        pass
    
    @abstractmethod
    async def read_trainee_history(self, user_id :str)-> list[TraineeHistory]:
        pass
    
    @abstractmethod
    async def upsert_trainee_history(self, trainee_history : TraineeHistory)-> TraineeHistory:
        pass
    
    @abstractmethod
    async def read_enrollments(self,coach_id:str | None, trainee_id :str | None)-> list[ProgramEnrollment]:
        pass
    
    @abstractmethod
    async def upsert_enrollment(self, program_enrollment : ProgramEnrollment)-> ProgramEnrollment:
        pass
    
    @abstractmethod
    async def read_coach_athletes_profile(self, coach_id:str )-> list[UserInDB]:
        pass
    
    @abstractmethod
    async def read_users_images_gallary(self,  users_id:list[str], tags:list[GallaryTag]) -> list[FileData]:
        pass
    
    @abstractmethod
    async def upsert_workout_program(self, workout_program : WorkoutProgram)-> WorkoutProgram:
        pass
    
    @abstractmethod
    async def read_workout_program(self, workout_id:str )-> WorkoutProgram:
        pass

    @abstractmethod
    async def initialize_workout_definition(self) -> None:
        pass
       
    @abstractmethod     
    async def read_exercise_definition(self) -> list[ExerciseDefinition]:
        pass

    @abstractmethod     
    async def upsert_referral(self,referral : Referral) -> Referral:
        pass
    
    @abstractmethod     
    async def read_referral_by_invite_contact(self,invite_contact : str) -> list[Referral]:
        pass
    
    @abstractmethod     
    async def read_referral_by_user_id(self,user_id : str) -> list[Referral]:
        pass
    @abstractmethod     
    async def read_referral_by_inviter_id(self,inviter_id : str) -> list[Referral]:
        pass
    @abstractmethod     
    async def read_coach_profiles(self,) -> list[UserInDB]:
        pass
    
    @abstractmethod     
    async def read_user_count(self, role : list[Role]) -> int | None:
        pass
    
    @abstractmethod     
    async def read_coaches_programs_count(self) -> int:
        pass

    @abstractmethod 
    async def coaches_purchased_programs_count(self, status: list[PaymentStatus])-> int:
        pass
    
    @abstractmethod 
    async def completed_exercise_count(self) -> int:
        pass