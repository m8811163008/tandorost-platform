

from data.common_data_model.language import Language # type: ignore
from .food_ai_model import (
    UserRequestedFood, 
    Ingredient, 
    CarbohydrateSource
    )

class CacheModel():


    @classmethod
    def system_instruction(cls):
        return f"""
                    Analyze the provided food input and identify its basic ingredients along with their approximate quantities.
                    Search for a food recipe in the provided language and find the best-matched recipe.
                    Return each ingredient as a separate Food object within the 'foods' list of the UserRequestedFood JSON object.
                    For composite dishes like stews or salads, list the primary ingredients.
                    For the calculated_calorie property in the Ingredient model, use the calorie of each unit_of_measurement_native_language multiplied by quantity_of_unit_of_measurement. As a helper reference, you can use unit_of_measurement_weight for calculating calories in each Ingredient.
                    For the total_fat_in_grams and total_carbohydrate_in_grams and total_protein_in_grams in the Ingredient model calculate based on total ingredient size for example in 2 spoons of olive oil we have 15 grams of oil in each spoon or unit_of_measurement_native_language and we have 2 or quantity_of_unit_of_measurement spoon and we have 15 grams of fat in each spoon so the total_fat_in_grams is 30 grams which is calculated by multiplying of quantity_of_unit_of_measurement by quantity of fat in each spoon based on your search result.
                    For onother example of the total_fat_in_grams and total_carbohydrate_in_grams and total_protein_in_grams in the Ingredient model calculate based on total ingredient size for example in 3 piece of apple we have 180 grams of apple in each piece or unit_of_measurement_native_language and we have 3 or quantity_of_unit_of_measurement piece and we have 1 grams of protien in each piece so the total_protein_in_grams is 3 grams which is calculated by multiplying of quantity_of_unit_of_measurement by quantity of protein in each piece based on your search result.
                    If the input is audio, generate the transcription first.

                    Example Input: '100 گرم املت'
                    The answer is: {CacheModel._food_example_1().model_dump_json(indent=2)}
                    Example Input: 'a simple salad with lettuce, cucumber, and olive oil'
                    The answer is: {CacheModel._food_example_2().model_dump_json(indent=2)}
                    Example Input: '200 grams of chicken breast and a cup of brown rice'
                    The answer is: {CacheModel._food_example_3().model_dump_json(indent=2)}
                    Example Input: 'یک عدد سیب و یک تکه نان بربری'
                    The answer is: {CacheModel._food_example_4().model_dump_json(indent=2)}
                    Example Input: 'یک بشقاب برنج و یک کاسه متوسط قرمه سبزی'
                    The answer is: {CacheModel._food_example_5().model_dump_json(indent=2)}
                    Example Input: 'a bowl of spaghetti with tomato sauce and meatballs'
                    The answer is: {CacheModel._food_example_6().model_dump_json(indent=2)}
                    Example Input: 'یک لیوان شیر و دو عدد خرما'
                    The answer is: {CacheModel._food_example_7().model_dump_json(indent=2)}
                    """

    @classmethod
    def _food_example_1(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=Language.PERSIAN,
                    user_native_language_ingredient_name='تخم مرغ',
                    translated_to_english_ingredient_name='egg',
                    unit_of_measurement_native_language='گرم',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=50,
                    quantity_of_unit_of_measurement=2,
                    calculated_calorie=150,
                    total_fat_in_grams=10.0,
                    total_carbohydrate_in_grams=1.0,
                    total_protein_in_grams=13.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='گوجه فرنگی',
                    translated_to_english_ingredient_name='tomato',
                    unit_of_measurement_native_language='گرم',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=30,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=18,
                    total_fat_in_grams=0.2,
                    total_carbohydrate_in_grams=4.0,
                    total_protein_in_grams=0.9,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='روغن',
                    translated_to_english_ingredient_name='oil',
                    unit_of_measurement_native_language='گرم',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=5,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=45,
                    total_fat_in_grams=5.0,
                    total_carbohydrate_in_grams=0.0,
                    total_protein_in_grams=0.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                )
            ]
        )


    @classmethod
    def _food_example_2(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='lettuce',
                    translated_to_english_ingredient_name='lettuce',
                    unit_of_measurement_native_language='gram',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=100,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=15,
                    total_fat_in_grams=0.2,
                    total_carbohydrate_in_grams=3.0,
                    total_protein_in_grams=1.0,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='cucumber',
                    translated_to_english_ingredient_name='cucumber',
                    unit_of_measurement_native_language='gram',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=50,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=8,
                    total_fat_in_grams=0.1,
                    total_carbohydrate_in_grams=2.0,
                    total_protein_in_grams=0.3,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='olive oil',
                    translated_to_english_ingredient_name='olive oil',
                    unit_of_measurement_native_language='ml',
                    translated_to_english_unit_of_measurement='ml',
                    unit_of_measurement_weight=15,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=120,
                    total_fat_in_grams=13.5,
                    total_carbohydrate_in_grams=0.0,
                    total_protein_in_grams=0.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                )
            ]
        )

    @classmethod
    def _food_example_3(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='chicken breast',
                    translated_to_english_ingredient_name='chicken breast',
                    unit_of_measurement_native_language='gram',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=100,
                    quantity_of_unit_of_measurement=2,
                    calculated_calorie=330,
                    total_fat_in_grams=7.0,
                    total_carbohydrate_in_grams=0.0,
                    total_protein_in_grams=62.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='brown rice',
                    translated_to_english_ingredient_name='brown rice',
                    unit_of_measurement_native_language='cup',
                    translated_to_english_unit_of_measurement='cup',
                    unit_of_measurement_weight=200,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=216,
                    total_fat_in_grams=1.8,
                    total_carbohydrate_in_grams=45.0,
                    total_protein_in_grams=5.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                )
            ]
        )
    
    @classmethod
    def _food_example_4(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='سیب',
                    translated_to_english_ingredient_name='apple',
                    unit_of_measurement_native_language='عدد',
                    translated_to_english_unit_of_measurement='piece',
                    unit_of_measurement_weight=180,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=95,
                    total_fat_in_grams=0.3,
                    total_carbohydrate_in_grams=25.0,
                    total_protein_in_grams=0.5,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='نان بربری',
                    translated_to_english_ingredient_name='barbari bread',
                    unit_of_measurement_native_language='تکه',
                    translated_to_english_unit_of_measurement='piece',
                    unit_of_measurement_weight=80,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=220,
                    total_fat_in_grams=1.0,
                    total_carbohydrate_in_grams=45.0,
                    total_protein_in_grams=7.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                )
            ]
        )

    @classmethod
    def _food_example_5(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='برنج',
                    translated_to_english_ingredient_name='rice',
                    unit_of_measurement_native_language='بشقاب',
                    translated_to_english_unit_of_measurement='plate',
                    unit_of_measurement_weight=150,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=200,
                    total_fat_in_grams=0.4,
                    total_carbohydrate_in_grams=44.0,
                    total_protein_in_grams=2.7,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='سبزی قورمه',
                    translated_to_english_ingredient_name='ghorme sabzi herbs',
                    unit_of_measurement_native_language='کاسه',
                    translated_to_english_unit_of_measurement='bowl',
                    unit_of_measurement_weight=100,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=50,
                    total_fat_in_grams=2.0,
                    total_carbohydrate_in_grams=5.0,
                    total_protein_in_grams=3.0,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='گوشت',
                    translated_to_english_ingredient_name='meat',
                    unit_of_measurement_native_language='گرم',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=100,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=250,
                    total_fat_in_grams=15.0,
                    total_carbohydrate_in_grams=0.0,
                    total_protein_in_grams=25.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='لوبیا قرمز',
                    translated_to_english_ingredient_name='red kidney beans',
                    unit_of_measurement_native_language='گرم',
                    translated_to_english_unit_of_measurement='gram',
                    unit_of_measurement_weight=50,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=170,
                    total_fat_in_grams=0.5,
                    total_carbohydrate_in_grams=30.0,
                    total_protein_in_grams=10.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='لیمو عمانی',
                    translated_to_english_ingredient_name='dried lime',
                    unit_of_measurement_native_language='عدد',
                    translated_to_english_unit_of_measurement='piece',
                    unit_of_measurement_weight=10,
                    quantity_of_unit_of_measurement=2,
                    calculated_calorie=30,
                    total_fat_in_grams=0.1,
                    total_carbohydrate_in_grams=7.0,
                    total_protein_in_grams=1.0,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                )
            ]
        )
    
    @classmethod
    def _food_example_6(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='spaghetti',
                    translated_to_english_ingredient_name='spaghetti',
                    unit_of_measurement_native_language='bowl',
                    translated_to_english_unit_of_measurement='bowl',
                    unit_of_measurement_weight=200,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=300,
                    total_fat_in_grams=1.5,
                    total_carbohydrate_in_grams=60.0,
                    total_protein_in_grams=11.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='tomato sauce',
                    translated_to_english_ingredient_name='tomato sauce',
                    unit_of_measurement_native_language='serving',
                    translated_to_english_unit_of_measurement='serving',
                    unit_of_measurement_weight=100,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=75,
                    total_fat_in_grams=3.0,
                    total_carbohydrate_in_grams=10.0,
                    total_protein_in_grams=2.0,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                ),
                Ingredient(
                    user_language=  Language.ENGLISH,
                    user_native_language_ingredient_name='meatballs',
                    translated_to_english_ingredient_name='meatballs',
                    unit_of_measurement_native_language='piece',
                    translated_to_english_unit_of_measurement='piece',
                    unit_of_measurement_weight=30,
                    quantity_of_unit_of_measurement=3,
                    calculated_calorie=60,
                    total_fat_in_grams=4.0,
                    total_carbohydrate_in_grams=2.0,
                    total_protein_in_grams=5.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                )
            ]
        )

    @classmethod
    def _food_example_7(cls):
        return UserRequestedFood(
            ingredients=[
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='شیر',
                    translated_to_english_ingredient_name='milk',
                    unit_of_measurement_native_language='لیوان',
                    translated_to_english_unit_of_measurement='glass',
                    unit_of_measurement_weight=240,
                    quantity_of_unit_of_measurement=1,
                    calculated_calorie=150,
                    total_fat_in_grams=8.0,
                    total_carbohydrate_in_grams=12.0,
                    total_protein_in_grams=8.0,
                    carbohydrate_source=CarbohydrateSource.OTHERS
                ),
                Ingredient(
                    user_language=  Language.PERSIAN,
                    user_native_language_ingredient_name='خرما',
                    translated_to_english_ingredient_name='date',
                    unit_of_measurement_native_language='عدد',
                    translated_to_english_unit_of_measurement='piece',
                    unit_of_measurement_weight=24,
                    quantity_of_unit_of_measurement=2,
                    calculated_calorie=140,
                    total_fat_in_grams=0.4,
                    total_carbohydrate_in_grams=37.0,
                    total_protein_in_grams=1.0,
                    carbohydrate_source=CarbohydrateSource.FRUITS_OR_NON_STARCHY_VEGETABLES
                )
            ]
        )