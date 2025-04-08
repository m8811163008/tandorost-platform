import os

class EnvirenmentVariable:

    @staticmethod
    def MONGO_URI() -> str:
        return os.environ.get("MONGO_URI") or EnvirenmentVariable._raise_env_error("MONGO_URI")

    @staticmethod
    def DATABASE_NAME() -> str:
        return os.environ.get("DATABASE_NAME") or EnvirenmentVariable._raise_env_error("DATABASE_NAME")

    @staticmethod
    def ACCESS_TOKEN_EXPIRE_MINUTES() -> int:
        value = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES") or EnvirenmentVariable._raise_env_error("ACCESS_TOKEN_EXPIRE_MINUTES")
        return int(value)

    @staticmethod
    def SECRET_KEY() -> str:
        return os.environ.get("SECRET_KEY") or EnvirenmentVariable._raise_env_error("SECRET_KEY")

    @staticmethod
    def ALGORITHM() -> str:
        return os.environ.get("ALGORITHM") or EnvirenmentVariable._raise_env_error("ALGORITHM")
    
    @staticmethod
    def _raise_env_error( var_name: str):
        raise EnvironmentError(f"Missing required environment variable: {var_name}")