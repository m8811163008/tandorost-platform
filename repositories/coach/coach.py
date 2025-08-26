

from data.local_database import DatabaseInterface
from data.local_database.model.coach import Coach
from data.local_database.model.coach_program import CoachProgram
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
        return await self.database.read_coach_by_user_id(user_id=user_id)

    async def upsert_coach_program(self, program: CoachProgram) -> CoachProgram:
        """Insert or update a coach program."""
        return await self.database.upsert_coach_program(program=program)

    async def delete_coach_program(self, program_id: str) -> None:
        """Delete a coach program by its ID."""
        await self.database.delete_coach_program(program_id=program_id)

    async def read_coach_programs(self, user_id: str) -> list[CoachProgram]:
        """Retrieve all coach programs for a user."""
        return await self.database.read_coach_programs(user_id=user_id)