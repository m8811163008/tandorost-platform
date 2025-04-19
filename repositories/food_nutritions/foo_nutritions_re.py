


from data.local_database import DatabaseInterface
from data.remote_api import  RemoteApiInterface




class FoodNutritionsRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api

    async def read_foods_nutritions_by_text(self, foods : str):
        # Todo recursively use models
        try:
            await self.remote_api.read_foods_nutritions_by_text(foods= foods,current_model_index =  0)
        except Exception as e:
            raise e