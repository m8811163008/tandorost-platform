
from datetime import datetime, timezone
from uuid import uuid4
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from typing import Any, Tuple

from pymongo import ReturnDocument
from data.local_database import Token
from data.local_database.local_database_interface import DatabaseInterface
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
from data.local_database.model.exceptions import DocumentNotFound, UserPhysicalDataValidationError
from data.local_database.model.program_enrollment import ExerciseDefinition, ProgramEnrollment, WorkoutProgram
from data.local_database.model.roles import Role
from data.local_database.model.trainee_history import TraineeHistory
from data.local_database.model.user import UserInDB
from data.local_database.model.user_food_count import UserFoodCount
from data.local_database.model.user_physical_data import DataPoint, UserPhysicalData, UserPhysicalDataUpsert
from data.local_database.model.user_files import (
    GallaryTag, 
    FileData, 
    ProcessingStatus
    )
from data.local_database.model.user_food import Food
from data.local_database.utility.exercisesDefinition import ExercisesDefinition
from data.remote_api.model.exceptions import NotFoundError
from data.local_database.model.user_subscription_payment_data import UserInDbSubscriptionPayment
from datetime import datetime



class LocalDataBaseImpl(DatabaseInterface):
    def __init__(self, uri: str, database_name: str):
        self.client: AsyncIOMotorClient[dict[str,Any]] = AsyncIOMotorClient(uri)
        self.db :AsyncIOMotorDatabase[dict[str,Any]] = self.client[database_name]
        self.user_collection : AsyncIOMotorCollection[dict[str,Any]] = self.db["UserCollection"]
        self.auth_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["TokenCollection"]
        self.user_physical_data_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserphysicalDataCollection"]
        self.user_static_file_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserStaticsFileCollection"]
        self.user_food_nutritions_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserFoodNutritionCollectionCollection"]
        self.user_subscription_payment_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["UserSubscriptionPaymentCollection"]
        self.coache_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["CoacheCollection"]
        self.coache_program_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["CoacheProgramCollection"]
        self.trainee_history_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["TraineeHistoryCollection"]
        self.enrollments_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["EnrollmentsCollection"]
        self.workout_program_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["WorkoutProgramCollection"]
        self.workout_definition_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["WorkoutDefinitionCollection"]
        self.najva_jan_ir_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["Najva-Jan-ir"]
        # self.trainer_collection : AsyncIOMotorCollection[dict[str, Any]] = self.db["TrainerCollection"]


    async def clear(self) -> None:
        await self.user_collection.delete_many({})
        await self.auth_collection.delete_many({})
        await self.user_physical_data_collection.delete_many({})
        await self.user_static_file_collection.delete_many({})
        await self.user_food_nutritions_collection.delete_many({})
        await self.user_subscription_payment_collection.delete_many({})
        await self.coache_collection.delete_many({})
        await self.coache_program_collection.delete_many({})
        await self.trainee_history_collection.delete_many({})
        await self.enrollments_collection.delete_many({})
        await self.workout_program_collection.delete_many({})
        await self.workout_definition_collection.delete_many({})
        await self.najva_jan_ir_collection.delete_many({})
        print('*****Database cleared!*****')

    async def _raise_for_invalid_user(self, user_id: str):
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            raise DocumentNotFound()
        
    async def read_user_by_identifier(self, identifier: str) -> UserInDB | None:
        user_data = await self.user_collection.find_one(
            {"$or": [{"phone_number": identifier}, {"email": identifier}]}
        )
        if user_data is None:
            return None
        return UserInDB(**user_data)
    
    async def read_user_by_id(self, user_id : str) -> UserInDB | None:
        """Retrieve a user token from the database."""
        user_data = await self.user_collection.find_one({"_id": user_id})
        if user_data is None:
            return None
        return UserInDB(**user_data)
    
    async def upsert_user(self, user: UserInDB)-> UserInDB:
        if user.id is None:
            user.id = str(uuid4())
        update_result = await self.user_collection.find_one_and_update(
            filter={"_id": user.id},
            update={"$set": user.model_dump(by_alias=True,exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER,
        )

        return UserInDB(**update_result)
        
    async def read_user_physical_data(self, user_id:str) -> UserPhysicalData | None:
        """Read user data"""
        user_physical_data = await self.user_physical_data_collection.find_one({"user_id": user_id})
        if user_physical_data is None:
            return None
        return UserPhysicalData(**user_physical_data)

    async def upsert_user_physical_data(self,user_id : str, user_physical_data: UserPhysicalDataUpsert)-> UserPhysicalData:
        """Update user data"""
        # await self.user_physical_data_collection.delete_many({})
        user_data = await self.user_physical_data_collection.find_one({"user_id":user_id})
        user_data_instance: UserPhysicalData
        current_datetime = datetime.now(timezone.utc)
        
        if user_data is None:
            if user_physical_data.birthday is None or user_physical_data.gender is None or user_physical_data.activity_level is None or user_physical_data.height is None or user_physical_data.weight is None:
                raise UserPhysicalDataValidationError(detail = 'age or gender or activity_level or height or weight is null')
            
            birth_datetime = datetime.combine(user_physical_data.birthday, datetime.min.time())

            user_data_instance = UserPhysicalData(
                _id = str(uuid4()),
                user_id = user_id,
                birthday = birth_datetime,
                gender = user_physical_data.gender,
                height= [DataPoint(data_point_id=str(uuid4()),value=user_physical_data.height, create_date=current_datetime)],
                weight= [DataPoint(data_point_id=str(uuid4()),value=user_physical_data.weight, create_date=current_datetime)],
                activity_level = [ DataPoint(data_point_id=str(uuid4()),value=user_physical_data.activity_level, create_date=current_datetime)],
                waist_circumference= [DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.waist_circumference] if value is not None],
                arm_circumference = [DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.arm_circumference] if value is not None],
                chest_circumference=[DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.chest_circumference] if value is not None],
                thigh_circumference=[DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.thigh_circumference] if value is not None],
                calf_muscle_circumference=[DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.calf_muscle_circumference] if value is not None],
                hip_circumference=[DataPoint(data_point_id=str(uuid4()),value=value, create_date=current_datetime) for value in [user_physical_data.hip_circumference] if value is not None],
            )
        else:
            user_data_instance = UserPhysicalData(**user_data)
    
            if user_physical_data.birthday is not None:
                birth_datetime = datetime.combine(user_physical_data.birthday, datetime.min.time())
                user_data_instance.birthday = birth_datetime
            if user_physical_data.gender is not None:
                user_data_instance.gender = user_physical_data.gender
            if user_physical_data.height is not None:
                user_data_instance.height.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.height,create_date=current_datetime))
            if user_physical_data.weight is not None:
                user_data_instance.weight.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.weight,create_date=current_datetime))
            if user_physical_data.activity_level is not None:
                user_data_instance.activity_level.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.activity_level,create_date=current_datetime))
            if user_physical_data.waist_circumference is not None:
                user_data_instance.waist_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.waist_circumference,create_date=current_datetime))
            if user_physical_data.arm_circumference is not None:
                user_data_instance.arm_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.arm_circumference,create_date=current_datetime))
            if user_physical_data.chest_circumference is not None:
                user_data_instance.chest_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.chest_circumference,create_date=current_datetime))
            if user_physical_data.thigh_circumference is not None:
                user_data_instance.thigh_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.thigh_circumference,create_date=current_datetime))
            if user_physical_data.calf_muscle_circumference is not None:
                user_data_instance.calf_muscle_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.calf_muscle_circumference,create_date=current_datetime))
            if user_physical_data.hip_circumference is not None:
                user_data_instance.hip_circumference.append(DataPoint(data_point_id=str(uuid4()),value=user_physical_data.hip_circumference,create_date=current_datetime))

        await self.user_physical_data_collection.find_one_and_update(
                filter={"user_id": user_id},
                update={"$set": user_data_instance.model_dump(exclude_none=True, by_alias=True)},
                return_document=ReturnDocument.AFTER,
                upsert=True
            )
        return user_data_instance
    
    async def delete_user_physical_data(self, user_id: str, data_point_id: str):
        user_data = await self.user_physical_data_collection.find_one({"user_id": user_id})
        if user_data is None:
            raise NotFoundError()
        user_physical_data = UserPhysicalData(**user_data)
        data_point_found = False
        for attribute in [
            "height",
            "weight",
            "activity_level",
            "waist_circumference",
            "arm_circumference",
            "chest_circumference",
            "thigh_circumference",
            "calf_muscle_circumference",
            "hip_circumference",
        ]:
            data_points = getattr(user_physical_data, attribute, [])

                
            
            updated_data_points = [
                dp for dp in data_points if dp.data_point_id != data_point_id
            ]
            if len(updated_data_points) < len(data_points):
                if(attribute == "height" or attribute == "weight" or attribute == "activity_level"):
                    if(len(data_points) == 1):
                        raise UserPhysicalDataValidationError(detail = 'activity_level or height or weight can not be empty')
                data_point_found = True
            setattr(user_physical_data, attribute, updated_data_points)
        
        if not data_point_found:
            raise NotFoundError()
        
        await self.user_physical_data_collection.find_one_and_update(
            filter={"user_id": user_id},
            update={"$set": user_physical_data.model_dump(exclude_none=True, by_alias=True)},
            return_document=ReturnDocument.AFTER,
            upsert=True,
        )
        
    
    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> list[FileData]:
        """Retrieve user image gallery based on tags."""
        result : list[FileData] = []
        for tag in tags:
            files = await self.user_static_file_collection.find({
                'user_id':user_id,
                'tag' : tag
            }).to_list()
            for file in files:
                result.append(FileData(**file))
        return result
            

    
    async def read_user_static_files(self,  user_id:str) -> list[FileData]:
        """Save a user token to the database."""
        result : list[FileData] = []
        files_dict = await self.user_static_file_collection.find({'user_id':user_id}).to_list()

        for file_dict in files_dict:
            result.append(FileData(**file_dict))
        return result
    
    
    async def upsert_user_files(self,  user_files:list[FileData]) -> list[FileData]:
        """Save a user token to the database."""
        if len(user_files) == 0:
            return user_files
        for user_file in user_files:
            if user_file.id is None:
                user_file.id = str(uuid4())
            await self.user_static_file_collection.find_one_and_update(
                filter={'_id': user_file.id},
                update={'$set': user_file.model_dump(by_alias=True, exclude_none=True)},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
        return user_files

    
    
    async def archive_images(self, images_id : list[str]) -> list[str] :
        """archive user images."""
        for image_id in images_id:
            await self.user_static_file_collection.find_one_and_update(
                filter={"_id": image_id},
                update={"$set": {
                    "processing_status" : ProcessingStatus.ARCHIVED 
                }},
                return_document=ReturnDocument.AFTER,
                upsert=True
            )
        return images_id



    # Auth methods
    async def upsert_token(self, token: Token) -> Token:
        """Save a user token to the database."""
        if token.id is None:
            token.id = str(uuid4())
        result =  await self.auth_collection.find_one_and_update(
            filter={'user_id': token.user_id},
            update={'$set' : token.model_dump(by_alias=True, exclude_none=True),},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return Token(**result)
    
    async def delete_token(self, user_id: str) -> None:
        """Save a user token to the database."""
        await self.auth_collection.find_one_and_delete(
            filter={'user_id': user_id},
        )
        
    

    async def read_token(self,  user_id:str) -> Token | None:
        """Save a user token to the database."""
        token = await self.auth_collection.find_one({'user_id' : user_id})
        if token is None:
            return None
        return Token(**token)
    

    async def read_user_foods(self,  user_id:str, start_date: datetime, end_date: datetime) -> list[Food]:
        user_foods = await self.user_food_nutritions_collection.find({
            'user_id':user_id,
            'upsert_date': {
                '$gte': start_date,
                '$lte': end_date
            }
        }).to_list()
        result: list[Food] = []
        for user_food in user_foods:
            result.append(Food(**user_food))
        return result

    async def upsert_user_foods(self, user_foods: list[Food]) -> list[Food]:
        if len(user_foods) == 0:
            return user_foods
        assert(user_foods[0].user_id is not None)

        for food in user_foods:
            if food.id == None:
                food.id = str(uuid4())
            await self.user_food_nutritions_collection.find_one_and_update(
                filter={'_id': food.id},
                update={'$set': food.model_dump(by_alias=True, exclude_none=True)},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
        return user_foods

    async def delete_user_foods(self, foods_ids: list[str]) -> list[str]:
        # Check if all food IDs exist
        existing_foods = await self.user_food_nutritions_collection.find(
            {"_id": {"$in": foods_ids}}
        ).to_list()

        if len(existing_foods) != len(foods_ids):
            missing_ids = set(foods_ids) - {food["_id"] for food in existing_foods}
            raise NotFoundError(message=str(missing_ids))

        # Delete all foods
        await self.user_food_nutritions_collection.delete_many(
            {"_id": {"$in": foods_ids}}
        )

        return foods_ids

    async def create_payment_subscription(self, subscription_data: UserInDbSubscriptionPayment):
        if subscription_data.id is None:
            subscription_data.id = str(uuid4())

        await self.user_subscription_payment_collection.find_one_and_update(
            filter={'_id': subscription_data.id},
            update={'$set': subscription_data.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return subscription_data
    
    async def read_payment_subscription(self, user_id :str )-> list[UserInDbSubscriptionPayment]:
        subscriptions = await self.user_subscription_payment_collection.find(
            {"user_id": user_id}
        ).to_list()
        
        return [UserInDbSubscriptionPayment(**sub) for sub in subscriptions]
    
    async def update_payment_subscription(self, payment_subscription :UserInDbSubscriptionPayment )-> UserInDbSubscriptionPayment:
        if payment_subscription.id is None:
            raise NotFoundError(message="Subscription ID is required for update")
        result = await self.user_subscription_payment_collection.find_one_and_update(
            filter={'_id': payment_subscription.id},
            update={'$set': payment_subscription.model_dump(by_alias=True, exclude_none=True)},
            upsert=False,
            return_document=ReturnDocument.AFTER
        )
        return UserInDbSubscriptionPayment(**result)


    async def read_user_food_counts(self, user_id :str )-> UserFoodCount:
        user_food_counts = await self.user_food_nutritions_collection.find(
            {"user_id": user_id},
            {"_id": 1}
        ).to_list()
        return UserFoodCount(count=len(user_food_counts))
    
    async def read_coach(self, user_id: str) -> Coach | None:
        coach_data = await self.coache_collection.find_one({'user_id': user_id})
        if coach_data is None:
            return None
        return Coach(**coach_data)


    async def upsert_coach(self, coach: Coach) -> Coach:
        # add id to update
        if coach.id is None:
            coach.id = str(uuid4())
        result = await self.coache_collection.find_one_and_update(
            filter={'_id': coach.id},
            update={'$set': coach.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return Coach(**result)

    async def upsert_coach_program(self, program: CoachProgram) -> CoachProgram:
        if program.id is None:
            program.id = str(uuid4())
        result = await self.coache_program_collection.find_one_and_update(
            filter={'_id': program.id},
            update={'$set': program.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return CoachProgram(**result)

    async def delete_coach_program(self, program_id: str) -> None:
        await self.coache_program_collection.find_one_and_delete(
            filter={'_id': program_id}
        )

    async def read_coach_programs(self, user_id: str) -> list[CoachProgram]:
        programs = await self.coache_program_collection.find({'user_id': user_id}).to_list()
        return [CoachProgram(**program) for program in programs]
    

    async def read_coaches(self)-> list[Coach]:
        coaches = await self.coache_collection.find({}).to_list()
        return [Coach(**coach) for coach in coaches]
    
    async def read_coaches_profile(self)-> list[UserInDB]:
        coachesProfile = await self.user_collection.find({"role": Role.BODYBUILDINGCOACH}).to_list()
        return [UserInDB(**coachProfile) for coachProfile in coachesProfile]
    
    async def read_trainee_history(self, user_id: str) -> list[TraineeHistory]:
        histories = await self.trainee_history_collection.find({'user_id': user_id}).to_list()
        return [TraineeHistory(**history) for history in histories]

    async def upsert_trainee_history(self, trainee_history: TraineeHistory) -> TraineeHistory:
        if trainee_history.id is None:
            trainee_history.id = str(uuid4())
        result = await self.trainee_history_collection.find_one_and_update(
            filter={'_id': trainee_history.id},
            update={'$set': trainee_history.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return TraineeHistory(**result)

    # async def read_trainees_by_coach(self, coach_id: str) -> list[UserInDB]:
    #     enrollments = await self.db["ProgramEnrollmentCollection"].find({'coach_id': coach_id}).to_list()
    #     trainee_ids = [enrollment['trainee_id'] for enrollment in enrollments]
    #     if not trainee_ids:
    #         return []
    #     trainees = await self.user_collection.find({'_id': {'$in': trainee_ids}}).to_list()
    #     return [UserInDB(**trainee) for trainee in trainees]


    async def read_enrollments(self, coach_id: str | None, trainee_id: str | None) -> list[ProgramEnrollment]:
        query = {}
        if coach_id is not None:
            query["coach_id"] = coach_id
        if trainee_id is not None:
            query["trainee_id"] = trainee_id
        enrollments = await self.enrollments_collection.find(query).to_list()
        return [ProgramEnrollment(**enrollment) for enrollment in enrollments]

    async def upsert_enrollment(self, program_enrollment: ProgramEnrollment) -> ProgramEnrollment:
        if program_enrollment.id is None:
            program_enrollment.id = str(uuid4())
        result = await self.enrollments_collection.find_one_and_update(
            filter={'_id': program_enrollment.id},
            update={'$set': program_enrollment.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return ProgramEnrollment(**result)
    
    async def read_coach_athletes_profile(self, coach_id: str) -> list[UserInDB]:
        enrollments = await self.enrollments_collection.find({'coach_id': coach_id}).to_list()
        trainee_ids = [enrollment['trainee_id'] for enrollment in enrollments]
        if not trainee_ids:
            return []
        athletes = await self.user_collection.find({'_id': {'$in': trainee_ids}}).to_list()
        return [UserInDB(**athlete) for athlete in athletes]
    
    async def read_users_images_gallary(self, users_id: list[str], tags: list[GallaryTag]) -> list[FileData]:
        result: list[FileData] = []
        query = {
            'user_id': {'$in': users_id},
            'tag': {'$in': tags}
        }
        files = await self.user_static_file_collection.find(query).to_list()
        for file in files:
            result.append(FileData(**file))
        return result
    
    async def upsert_workout_program(self, workout_program: WorkoutProgram) -> WorkoutProgram:
        if workout_program.id is None:
            workout_program.id = str(uuid4())
        result = await self.workout_program_collection.find_one_and_update(
            filter={'_id': workout_program.id},
            update={'$set': workout_program.model_dump(by_alias=True, exclude_none=True)},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return WorkoutProgram(**result)
    
    async def initialize_workout_definition(self) -> None:
        for exercise in ExercisesDefinition.exercises:
            if exercise.id is None:
                exercise.id = str(uuid4())
            
            await self.workout_definition_collection.find_one_and_update(
                filter={"_id": exercise.id},
                update={"$set": exercise.model_dump(by_alias=True)},
                upsert=True,
                return_document=ReturnDocument.AFTER
            )
            
    async def read_exercise_definition(self) -> list[ExerciseDefinition]:
        exercises = await self.workout_definition_collection.find({}).to_list()
        if not exercises:
            await self.initialize_workout_definition()
            exercises = await self.workout_definition_collection.find({}).to_list()
        return [ExerciseDefinition(**exercise) for exercise in exercises]

    async def read_workout_program(self, workout_id: str) -> WorkoutProgram:
        program = await self.workout_program_collection.find_one({'_id': workout_id})
        return WorkoutProgram(**program)
    
    
    async def save_najva_sms_to_local(self, numbers: list[str]) -> Tuple[list[str], int]:
        # 1. Fetch saved numbers
        saved_docs = await self.najva_jan_ir_collection.find({}, {"_id": 0, "number": 1}).to_list()
        saved_numbers = set(doc["number"] for doc in saved_docs if "number" in doc)

        # 2. Normalize numbers to a standard format (e.g., always start with +98)
        def normalize_number(num: str) -> str:
            n = num.strip()
            if n.startswith("+98"):
                return n
            if n.startswith("0098"):
                return "+" + n[2:]
            if n.startswith("98"):
                return "+98" + n[2:]
            if n.startswith("0") and len(n) == 11:
                return "+98" + n[1:]
            return n

        normalized_saved = set(normalize_number(n) for n in saved_numbers)
        normalized_input = set(normalize_number(n) for n in numbers)

        # 3. Remove duplicates (already saved)
        to_save = normalized_input - normalized_saved

        # 4. Save not duplicated numbers to collection
        if to_save:
            await self.najva_jan_ir_collection.insert_many([{"number": n} for n in to_save])
        count = await self.najva_jan_ir_collection.count_documents({})
        return list(to_save), count