


from data.local_database import DatabaseInterface
from data.remote_api import  RemoteApiInterface
from data.remote_api.model.food_ai_model import AudioMemeType




class FoodNutritionsRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api

    async def read_foods_nutritions_by_text(self, foods : str):
        # Todo recursively use models
        try:
            return await self.remote_api.read_foods_nutritions_by_text(foods= foods)
        except Exception as e:
            raise e
        
    async def read_foods_nutritions_by_voice(self, meme_type: AudioMemeType, foods : bytes ):
        # Todo recursively use models
        try:
            return await self.remote_api.read_foods_nutritions_by_voice(foods= foods, meme_type = meme_type)
        except Exception as e:
            raise e