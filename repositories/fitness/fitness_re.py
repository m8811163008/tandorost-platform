from data.local_database.local_database_interface import DatabaseInterface
from data.local_database.model.user_bio_data import ActivityLevel, Gender
from domain_models.fitness_data import FitnessData


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
    
    