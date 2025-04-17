from data.local_database import LocalDataBaseImpl
from repositories.user_files.user_files import UserFiles
from utility import EnvirenmentVariable
from data.remote_api import RemoteApiImpl
from domain_models import SMSPanelCongif
from repositories.auth import AuthRepository
from repositories.user import UserRepository

class DependencyManager():
    def __init__(self) -> None:
        # Initialize data layers
        self.local_database = LocalDataBaseImpl(uri=EnvirenmentVariable.MONGO_URI(), database_name=EnvirenmentVariable.DATABASE_NAME())
        self.remote_database = RemoteApiImpl(config= SMSPanelCongif(username=EnvirenmentVariable.SMS_PANEL_USERNAME(), password=EnvirenmentVariable.SMS_PANEL_PASSWORD()))

        # Initialize repository layers
        self.auth_repo = AuthRepository(database=self.local_database,remote_api= self.remote_database)
        self.user_repo = UserRepository(database=self.local_database)
        self.user_files_repo = UserFiles(database=self.local_database)

dm = DependencyManager()