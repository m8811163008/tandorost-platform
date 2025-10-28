
from data.remote_api.model.email_config import EmailSMTPCongif
from repositories.coach.coach import CoachRepository
from repositories.fitness.fitness_re import FitnessRepository
from repositories.payment.payment import PaymentRepository
from repositories.user_files.user_files_re import UserFiles
from utility import EnvirenmentVariable
from data.remote_api import RemoteApiImpl
from domain_models import SMSPanelCongif, GeminiConfig
from repositories.auth import AuthRepository
from repositories.user import UserRepository
from repositories.food_nutritions import FoodNutritionsRepository
from utility.constants import  verification_sms_panel_body_id,invite_sms_panel_body_id

class DependencyManager():
    def __init__(self) -> None:
        # Initialize data layers
        from data.local_database import LocalDataBaseImpl
        self.local_database = LocalDataBaseImpl(uri=EnvirenmentVariable.MONGO_URI(), database_name=EnvirenmentVariable.DATABASE_NAME())
        self.sms_config = SMSPanelCongif(username=EnvirenmentVariable.SMS_PANEL_USERNAME(), password=EnvirenmentVariable.SMS_PANEL_PASSWORD())
        self.ai_config = GeminiConfig(api_key=EnvirenmentVariable.GEMENI_API_KEY() )
        self.email_config = EmailSMTPCongif(username=EnvirenmentVariable.EMAILSMTPUSERNAME(), appPassword=EnvirenmentVariable.EMAILSMTPAPPPASSWORD(), host=EnvirenmentVariable.EMAILSMTPHOST(), port=EnvirenmentVariable.EMAILSMTPPORT())
        self.remote_database = RemoteApiImpl(sms_config = self.sms_config,email_config=self.email_config, ai_config = self.ai_config )

        # Initialize repository layers
        self.auth_repo = AuthRepository(database=self.local_database,remote_api= self.remote_database, sms_body_id=verification_sms_panel_body_id)
        self.food_nutrition_repo = FoodNutritionsRepository(database=self.local_database,remote_api= self.remote_database)
        self.user_repo = UserRepository(database=self.local_database, remote_api=self.remote_database,sms_body_id=invite_sms_panel_body_id )
        self.user_files_repo = UserFiles(database=self.local_database)
        self.fitness_repo = FitnessRepository(database = self.local_database)
        self.payment_repo = PaymentRepository(database = self.local_database)
        self.coach_repo = CoachRepository(database = self.local_database)


dm = DependencyManager()