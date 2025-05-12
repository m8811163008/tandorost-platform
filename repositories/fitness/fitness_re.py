from data.local_database.local_database_interface import DatabaseInterface
from data.local_database.model.change_weight_speed import ChangeWeightSpeed
from data.local_database.model.user_bio_data import ActivityLevel, Gender
from domain_models.fitness_data import FitnessData
from domain_models.nutrition_requrement import NutritionRequerment, NutritionRequerments


class FitnessRepository:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    async def fitness_data(self,user_id:str) -> FitnessData | None:
        user = await self.database.read_user_bio_data(user_id=user_id)
        if user is None:
            return None
        
        weight = user.weight[-1].value
        assert(isinstance(weight, float))

        height = user.height[-1].value
        assert(isinstance(height, float))

        is_male = user.gender == Gender.MALE
        age = user.age

        # Energy used for breathing and diegstion and maintain the body temperture.
        # It cacultaed base on age and weight and height and gender base on Mufflin st geor formulla.
        resting_metabolic_rate = 10 * weight + 6.25 * height - 5 * age + (5 if is_male else -161)

        activity_level = user.activity_level[-1]
        assert(isinstance(activity_level, ActivityLevel))

        total_daily_energy_expenditure = resting_metabolic_rate * activity_level.multiplier

        is_waist_circumference_exist = len(user.waist_circumference) != 0

        waist_circumference_to_height_ratio = None
        is_waist_circumference_to_height_ratio_safe = None
        is_waist_circumference_safe_range = None 

        if is_waist_circumference_exist:
            waistCircumference = user.waist_circumference[-1]
            assert(isinstance(waistCircumference, float))

            waist_circumference_to_height_ratio = waistCircumference / height
            # To predict diabtes type 2 and blood presure and cardio(heart and arthritis) disease and bale grader disease
            is_waist_circumference_to_height_ratio_safe = waist_circumference_to_height_ratio < 0.5
            # Is waistCircumference is less than 94 in men and less than 80 in women.
            is_waist_circumference_safe_range = waistCircumference < 94 if is_male else waistCircumference < 80

        bmi = weight / ((height / 100) ** 2)

        return FitnessData(
            resting_metabolic_rate=resting_metabolic_rate,
            total_daily_energy_expenditure = total_daily_energy_expenditure,
            bmi=bmi,
            waist_circumference_to_height_ratio = waist_circumference_to_height_ratio ,
            is_waist_circumference_to_height_ratio_safe = is_waist_circumference_to_height_ratio_safe ,
            is_waist_circumference_safe_range = is_waist_circumference_safe_range 
        )
    
    
    async def nutrition_requerment_data(self,user_id:str) -> NutritionRequerments:
        user = await self.database.read_user_by_id(user_id=user_id)
        assert(user is not None)
        user_bio_data = await self.database.read_user_bio_data(user_id=user_id)
        assert(user_bio_data is not None)
        fitness_data = await self.fitness_data(user_id=user_id)
        assert(fitness_data is not None)

        assert(len(user_bio_data.activity_level) != 0)
        activity_level = user_bio_data.activity_level[-1]
        assert(activity_level is ActivityLevel)
        weight = user_bio_data.weight[-1]
        assert(weight is float)
        age = user_bio_data.age
        # Daily requirement of total energy expenditure based on [dayActivityLevel] and [changeWeightSpeed].
        change_weight_speed = user.change_weight_speed
        # rest day
        effective_total_daily_energy_expenditure_on_rest_day = fitness_data.total_daily_energy_expenditure * (1 - change_weight_speed.value.rest_day_change_value)
        # traning day
        effective_total_daily_energy_expenditure_on_training_day = fitness_data.total_daily_energy_expenditure * (1 - change_weight_speed.value.training_day_change_value)

        # 9 kcal in each grams of fat
        # 35% of totalDailyEnergyExpenditure should be helthy fats.
        # 10% saturated and 12% mono unsaturated and 13% polysaturated.
        fat_on_rest_day = int(effective_total_daily_energy_expenditure_on_rest_day * 0.35 / 9)
        fat_on_training_day = int(effective_total_daily_energy_expenditure_on_training_day * 0.35 / 9)

        # 4 kcal in each gram of protein
        protein_per_kilogram_per_day_on_rest_day = self._calculate_protein(change_weight_speed = change_weight_speed, activity_level=activity_level, is_trainig_day=False, age=age)
        protein_per_kilogram_per_day_on_training_day = self._calculate_protein(change_weight_speed = change_weight_speed, activity_level=activity_level,  is_trainig_day=True, age=age)
        protein_on_rest_day = protein_per_kilogram_per_day_on_rest_day * weight
        protein_on_training_day = protein_per_kilogram_per_day_on_training_day * weight
        
        # 4 kcal in each grams of carbohydrate
        # totalDailyEnergyExpenditure - fatCalorie - proteinCalorie
        # on rest day 66% of carb is FRUITS_OR_NON_STARCHY_VEGETABLES
        carbohydrate_calorie_on_rest_day = effective_total_daily_energy_expenditure_on_rest_day - fat_on_rest_day * 9 - protein_on_rest_day * 4
        carbohydrate_calorie_on_training_day = effective_total_daily_energy_expenditure_on_training_day - fat_on_training_day * 9 - protein_on_training_day * 4

        carbohydrate_fruits_or_non_starchy_vegetables_on_rest_day = (carbohydrate_calorie_on_rest_day * 0.66) / 4
        carbohydrate_none_fruits_or_non_starchy_vegetables_on_rest_day = (carbohydrate_calorie_on_rest_day * 0.34) / 4
        carbohydrate_fruits_or_non_starchy_vegetables_on_training_day = (carbohydrate_calorie_on_training_day * 0.33) / 4
        carbohydrate_none_fruits_or_non_starchy_vegetables_on_training_day = (carbohydrate_calorie_on_training_day * 0.67) / 4

        rest_day = NutritionRequerment(fat = fat_on_rest_day, protein=protein_on_rest_day, carbohydrate_fruits_or_non_starchy_vegetables=carbohydrate_fruits_or_non_starchy_vegetables_on_rest_day, carbohydrate_other=carbohydrate_none_fruits_or_non_starchy_vegetables_on_rest_day)
        training_day = NutritionRequerment(fat=fat_on_training_day , protein=protein_on_training_day, carbohydrate_fruits_or_non_starchy_vegetables=carbohydrate_fruits_or_non_starchy_vegetables_on_training_day, carbohydrate_other=carbohydrate_none_fruits_or_non_starchy_vegetables_on_training_day)
        return NutritionRequerments(rest_day=rest_day, training_day=training_day)


    def _calculate_protein(self,change_weight_speed: ChangeWeightSpeed, activity_level: ActivityLevel, is_trainig_day : bool, age:int) -> float:
        if(change_weight_speed != ChangeWeightSpeed.CONSTANT):
            # Losing weight 1.8–2.7 g/kg BW/day
            match activity_level:
                case ActivityLevel.SEDENTARY:
                    return 2
                case ActivityLevel.FAIRLY_ACTIVE:
                    return 2.2 if is_trainig_day else 2.1
                case ActivityLevel.MODERATELY_ACTIVE:
                    return 2.3 if is_trainig_day else 2.2
                case ActivityLevel.ACTIVE:
                    return 2.4 if is_trainig_day else 2.3
                case ActivityLevel.VERY_ACTIVE:
                    return 2.7 if is_trainig_day else 2.5
                case _:
                    raise Exception('ActivityLevel is not valid value')
        else:
            # Not losing weight with training program 1.3-1.7 g/kg BW/day
            # Not losing weight without training program 0.75 g/kg BW/day
            # Not losing weight 1.2–1.5 g/kg BW/day over 50 years old
            match activity_level:
                case ActivityLevel.SEDENTARY:
                    return 1.4 if age >= 50 else 0.75
                case ActivityLevel.FAIRLY_ACTIVE:
                    return 1.5 if is_trainig_day else 1.3
                case ActivityLevel.MODERATELY_ACTIVE:
                    return 1.6 if is_trainig_day else 1.5
                case ActivityLevel.ACTIVE:
                    return 1.7 if is_trainig_day else 1.5
                case ActivityLevel.VERY_ACTIVE:
                    return 1.7 if is_trainig_day else 1.6
                case _:
                    raise Exception('ActivityLevel is not valid value')