

from data.local_database import DatabaseInterface
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
from data.local_database.model.program_enrollment import ExerciseDefinition, ProgramEnrollment, WorkoutProgram
from data.local_database.model.trainee_history import TraineeHistory
from data.local_database.model.user_physical_data import UserPhysicalData
from domain_models import  UserInDB, UserPhysicalDataUpsert

class CoachRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    async def upsert_coach(self, coach: Coach) -> Coach:
        """Insert or update a coach in the database."""
        return await self.database.upsert_coach(coach=coach)

    async def read_coach(self, user_id: str) -> Coach | None:
        """Retrieve a coach by user_id."""
        return await self.database.read_coach(user_id=user_id)

    async def upsert_coach_program(self, program: CoachProgram) -> CoachProgram:
        """Insert or update a coach program."""
        return await self.database.upsert_coach_program(program=program)

    async def delete_coach_program(self, program_id: str) -> None:
        """Delete a coach program by its ID."""
        await self.database.delete_coach_program(program_id=program_id)

    async def read_coach_programs(self, user_id: str) -> list[CoachProgram]:
        """Retrieve all coach programs for a user."""
        return await self.database.read_coach_programs(user_id=user_id)
    
    async def read_coaches(self )-> list[Coach]:
        return await self.database.read_coaches()
    
    async def read_coaches_profile(self )-> list[UserInDB]:
        return await self.database.read_coaches_profile()
    
    
    async def read_trainee_history(self, user_id :str)-> list[TraineeHistory]:
        return await self.database.read_trainee_history(user_id = user_id)
    
    
    async def upsert_trainee_history(self, trainee_history : TraineeHistory)-> TraineeHistory:
        return await self.database.upsert_trainee_history(trainee_history = trainee_history)
    
    async def read_enrollments(self, coach_id: str | None, trainee_id: str | None) -> list[ProgramEnrollment]:
        return await self.database.read_enrollments(coach_id = coach_id, trainee_id = trainee_id)

    async def upsert_enrollment(self, program_enrollment: ProgramEnrollment) -> ProgramEnrollment:
        return await self.database.upsert_enrollment(program_enrollment = program_enrollment)
    
    async def read_coach_athletes_profile(self, coach_id:str )-> list[UserInDB]:
        return await self.database.read_coach_athletes_profile(coach_id = coach_id)
    

    async def upsert_workout_program(self, workout_program : WorkoutProgram)-> WorkoutProgram:
        return await self.database.upsert_workout_program(workout_program = workout_program)
    

    async def read_workout_program(self, workout_id:str )-> WorkoutProgram:
        return await self.database.read_workout_program(workout_id = workout_id)
    
    async def read_exercise_definition(self )-> list[ExerciseDefinition]:
        return await self.database.read_exercise_definition()
    
    async def read_coach_profiles(self )-> list[UserInDB]:
        return await self.database.read_coach_profiles()
    