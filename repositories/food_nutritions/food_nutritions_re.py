


from datetime import datetime
from uuid import uuid4
from data.local_database import DatabaseInterface
from data.local_database.model.user_food import CarbohydrateSourceLD, TotalMacroNutritionPerFood
from data.remote_api import  RemoteApiInterface
from data.remote_api.model.food_ai_model import AudioMemeType
from domain_models import  UserRequestedFood, Food, CarbohydrateSource


class FoodNutritionsRepository:
    def __init__(self, database: DatabaseInterface, remote_api:RemoteApiInterface):
        self.database = database
        self.remote_api = remote_api

    async def read_foods_nutritions_by_text(self,user_id: str, foods : str) -> list[Food]:
        # Todo recursively use models
        try:
            user_requested_food = await self.remote_api.read_foods_nutritions_by_text(foods= foods)
            return await self._upsert_foods_on_database(user_id = user_id, user_requested_food=user_requested_food, )
        except Exception as e:
            raise e
        
    async def read_foods_nutritions_by_voice(self,user_id: str, meme_type: AudioMemeType, foods : bytes ):
        # Todo recursively use models
        try:
            user_requested_food = await self.remote_api.read_foods_nutritions_by_voice(foods= foods, meme_type = meme_type)
            return await self._upsert_foods_on_database(user_id = user_id, user_requested_food=user_requested_food, )
        except Exception as e:
            raise e
        
    async def read_foods_nutritions(self,user_id: str,start_date: datetime,end_date: datetime) -> list[Food]:
        return await self.database.read_user_foods(user_id=user_id, start_date=start_date, end_date=end_date)
    
    async def delete_user_foods(self,foods_ids: list[str]) -> list[str]:
        return await self.database.delete_user_foods(foods_ids=foods_ids)
    
    async def update_user_food(self,food: Food) -> Food:
        result = await self.database.upsert_user_foods(user_foods=[food])
        return result[0]
        
    async def _upsert_foods_on_database(self,user_id :str,   user_requested_food:UserRequestedFood)-> list[Food]:
        foods_list : list[Food]= []
        upsert_date = datetime.now()
        for ingredient in user_requested_food.ingredients:
            food = Food(
                user_id=user_id,
                id = str(uuid4()),
                upsert_date=upsert_date,
                user_language = ingredient.user_language,
                user_native_language_food_name = ingredient.user_native_language_ingredient_name,
                translated_to_english_food_name= ingredient.translated_to_english_ingredient_name,
                unit_of_measurement_native_language = ingredient.unit_of_measurement_native_language,
                translated_to_english_unit_of_measurement = ingredient.translated_to_english_unit_of_measurement,
                calculated_calorie = ingredient.calculated_calorie,
                quantity_of_unit_of_measurement= ingredient.quantity_of_unit_of_measurement,
                carbohydrate_source=self._map_carbohydrate_source(ingredient.carbohydrate_source) ,
                macro_nutrition= TotalMacroNutritionPerFood(
                    fat= ingredient.total_fat_in_grams,
                    carbohydrate= ingredient.total_carbohydrate_in_grams,
                    protein= ingredient.total_protein_in_grams
                )
            ) 
            foods_list.append(food)

        return await self.database.upsert_user_foods(user_foods=foods_list)    
        
    def _map_carbohydrate_source(self, source: CarbohydrateSource) -> CarbohydrateSourceLD:
        if source == CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES:
            return CarbohydrateSourceLD.FRUITS_OR_NON_STARCHY_VEGETABLES
        elif source == CarbohydrateSource.OTHERS:
            return CarbohydrateSourceLD.OTHERS
        else:
            raise ValueError('CarbohydrateSource unknown')