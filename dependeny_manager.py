from data.local_database.local_database_impl import LocalDataBaseImpl
from utility.envirement_variables import EnvirenmentVariable
from data.remote_api.remote_api_impl import RemoteApiImpl
from domain_models.data_models import SMSPanelCongif
from repositories.auth.auth_re import AuthRepository
from repositories.user.user import UserRepository

class DependencyManager():
    def __init__(self) -> None:
        # Initialize data layers
        self.local_database = LocalDataBaseImpl(uri=EnvirenmentVariable.MONGO_URI(), database_name=EnvirenmentVariable.DATABASE_NAME())
        self.remote_database = RemoteApiImpl(config= SMSPanelCongif(username='', password=''))

        # Initialize repository layers
        self.auth_repo = AuthRepository(database=self.local_database,remote_api= self.remote_database)
        self.user_repo = UserRepository(database=self.local_database)

dm = DependencyManager()