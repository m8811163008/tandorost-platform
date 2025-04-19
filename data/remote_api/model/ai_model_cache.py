
from google import genai, ModelSelectionConfig # type: ignore
from google.genai import types # type: ignore

from domain_models.food_ai_model import (
    UserRequestedFood, 
    Food, 
    UserLanguage, 
    CarbohydrateSource
    )

class CacheModel():


    @property
    def system_instruction(self):
        return f"""
        Analyze the provided food input and identify its basic ingredients along with their approximate quantities.
        Return each ingredient as a separate Food object within the 'foods' list of the UserRequestedFood JSON object.
        For composite dishes like stews or salads, list the primary ingredients.
        If the input is audio, generate the transcription first.

        Example Input: '100 گرم املت'
        The answer is: {self._food_example_1.model_dump_json(indent=2)}
        Example Input: 'a simple salad with lettuce, cucumber, and olive oil'
        The answer is: {self._food_example_2.model_dump_json(indent=2)}
        Example Input: '200 grams of chicken breast and a cup of brown rice'
        The answer is: {self._food_example_3.model_dump_json(indent=2)}
        Example Input: 'یک عدد سیب و یک تکه نان بربری'
        The answer is: {self._food_example_4.model_dump_json(indent=2)}
        Example Input: 'یک بشقاب برنج و یک کاسه متوسط قرمه سبزی'
        The answer is: {self._food_example_5_corrected.model_dump_json(indent=2)}
        """

    @property
    def _food_example_1(self):
        return UserRequestedFood(
            foods=[
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="تخم مرغ",
                    translated_to_english_food_name="egg",
                    unit_of_measurement_native_language="عدد",
                    translated_to_english_unit_of_measurement="count",
                    calorie_per_unit_of_measurement=70,  # Approximate calorie per egg
                    weight_per_unit_of_measurement=50,  # Approximate weight per egg in grams
                    quantity_of_unit_of_measurement=2,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="گوجه فرنگی",
                    translated_to_english_food_name="tomato",
                    unit_of_measurement_native_language="عدد",
                    translated_to_english_unit_of_measurement="count",
                    calorie_per_unit_of_measurement=22,  # Approximate calorie per tomato
                    weight_per_unit_of_measurement=100,  # Approximate weight per tomato in grams
                    quantity_of_unit_of_measurement=2,  # Assuming a portion of a tomato
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="روغن مایع",
                    translated_to_english_food_name="cooking oil",
                    unit_of_measurement_native_language="قاشق غذاخوری",
                    translated_to_english_unit_of_measurement="tablespoon",
                    calorie_per_unit_of_measurement=120,  # Approximate calorie per tablespoon of oil
                    weight_per_unit_of_measurement=14,  # Approximate weight per tablespoon of oil in grams
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
            ]
        )


    @property
    def _food_example_2(self):
        return UserRequestedFood(
            foods=[
                Food(
                    user_language=UserLanguage.EN,
                    user_native_language_food_name="lettuce",
                    translated_to_english_food_name="lettuce",
                    unit_of_measurement_native_language="cup",
                    translated_to_english_unit_of_measurement="cup",
                    calorie_per_unit_of_measurement=5,
                    weight_per_unit_of_measurement=85,
                    quantity_of_unit_of_measurement=2,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES,
                ),
                Food(
                    user_language=UserLanguage.EN,
                    user_native_language_food_name="cucumber",
                    translated_to_english_food_name="cucumber",
                    unit_of_measurement_native_language="slice",
                    translated_to_english_unit_of_measurement="slice",
                    calorie_per_unit_of_measurement=2,
                    weight_per_unit_of_measurement=10,
                    quantity_of_unit_of_measurement=10,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES,
                ),
                Food(
                    user_language=UserLanguage.EN,
                    user_native_language_food_name="olive oil",
                    translated_to_english_food_name="olive oil",
                    unit_of_measurement_native_language="tablespoon",
                    translated_to_english_unit_of_measurement="tablespoon",
                    calorie_per_unit_of_measurement=120,
                    weight_per_unit_of_measurement=14,
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
            ]
        )

    @property
    def _food_example_3(self):
        return UserRequestedFood(
            foods=[
                Food(
                    user_language=UserLanguage.EN,
                    user_native_language_food_name="chicken breast",
                    translated_to_english_food_name="chicken breast",
                    unit_of_measurement_native_language="gram",
                    translated_to_english_unit_of_measurement="gram",
                    calorie_per_unit_of_measurement=165, # Approximate calories per 100 grams
                    weight_per_unit_of_measurement=100,
                    quantity_of_unit_of_measurement=200,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
                Food(
                    user_language=UserLanguage.EN,
                    user_native_language_food_name="brown rice",
                    translated_to_english_food_name="brown rice",
                    unit_of_measurement_native_language="cup",
                    translated_to_english_unit_of_measurement="cup",
                    calorie_per_unit_of_measurement=216, # Approximate calories per cooked cup
                    weight_per_unit_of_measurement=195,
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
            ]
        )

    @property
    def _food_example_4(self):
        return UserRequestedFood(
            foods=[
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="سیب",
                    translated_to_english_food_name="apple",
                    unit_of_measurement_native_language="عدد",
                    translated_to_english_unit_of_measurement="count",
                    calorie_per_unit_of_measurement=95, # Approximate calories per medium apple
                    weight_per_unit_of_measurement=182,
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="نان بربری",
                    translated_to_english_food_name="barbari bread",
                    unit_of_measurement_native_language="تکه",
                    translated_to_english_unit_of_measurement="piece",
                    calorie_per_unit_of_measurement=200, # Approximate calories per standard piece
                    weight_per_unit_of_measurement=75,
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
            ]
        )

    @property
    def _food_example_5_corrected(self):
        return UserRequestedFood(
            foods=[
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="برنج",
                    translated_to_english_food_name="rice",
                    unit_of_measurement_native_language="بشقاب",
                    translated_to_english_unit_of_measurement="plate",
                    calorie_per_unit_of_measurement=200, # Approximate calories per plate
                    weight_per_unit_of_measurement=150, # Approximate weight in grams
                    quantity_of_unit_of_measurement=1,
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="گوشت گوسفند",
                    translated_to_english_food_name="lamb meat",
                    unit_of_measurement_native_language="گرم",
                    translated_to_english_unit_of_measurement="gram",
                    calorie_per_unit_of_measurement=280, # Approximate calories per 100 grams
                    weight_per_unit_of_measurement=100,
                    quantity_of_unit_of_measurement=75, # Approximate amount in a medium bowl
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="لوبیا قرمز",
                    translated_to_english_food_name="kidney beans",
                    unit_of_measurement_native_language="گرم",
                    translated_to_english_unit_of_measurement="gram",
                    calorie_per_unit_of_measurement=130, # Approximate calories per 100 grams (cooked)
                    weight_per_unit_of_measurement=100,
                    quantity_of_unit_of_measurement=50, # Approximate amount in a medium bowl
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="سبزی قرمه",
                    translated_to_english_food_name="ghormeh sabzi herbs",
                    unit_of_measurement_native_language="گرم",
                    translated_to_english_unit_of_measurement="gram",
                    calorie_per_unit_of_measurement=50, # Approximate calories per 100 grams
                    weight_per_unit_of_measurement=30, # Approximate amount in a medium bowl
                    quantity_of_unit_of_measurement=50,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES,
                ),
                Food(
                    user_language=UserLanguage.FA,
                    user_native_language_food_name="روغن",
                    translated_to_english_food_name="oil",
                    unit_of_measurement_native_language="قاشق غذاخوری",
                    translated_to_english_unit_of_measurement="tablespoon",
                    calorie_per_unit_of_measurement=120, # Approximate calories per tablespoon
                    weight_per_unit_of_measurement=14,
                    quantity_of_unit_of_measurement=2, # Approximate amount in a medium bowl
                    carbohydrate_source=CarbohydrateSource.OTHERS,
                ),
            ]
        )