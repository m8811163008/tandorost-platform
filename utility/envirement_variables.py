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
    def SMS_PANEL_USERNAME() -> str:
        return os.environ.get("SMS_PANEL_USERNAME") or EnvirenmentVariable._raise_env_error("SMS_PANEL_USERNAME")
    
    @staticmethod
    def SMS_PANEL_PASSWORD() -> str:
        return os.environ.get("SMS_PANEL_PASSWORD") or EnvirenmentVariable._raise_env_error("SMS_PANEL_PASSWORD")
    
    @staticmethod
    def GEMENI_API_KEY() -> str:
        return os.environ.get("GEMENI_API_KEY") or EnvirenmentVariable._raise_env_error("GEMENI_API_KEY")
    
    @staticmethod
    def CAFFE_BAZZAR_RSA() -> str:
        return os.environ.get("CAFFE_BAZZAR_RSA") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_RSA")

    @staticmethod
    def CAFFE_BAZZAR_SUBSCRIPTION_PLAN_ONE_MONTH_SDK() -> str:
        return os.environ.get("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_ONE_MONTH_SDK") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_ONE_MONTH_SDK")

    @staticmethod
    def CAFFE_BAZZAR_SUBSCRIPTION_PLAN_THREE_MONTH_SDK() -> str:
        return os.environ.get("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_THREE_MONTH_SDK") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_THREE_MONTH_SDK")
    
    @staticmethod
    def CAFFE_BAZZAR_SUBSCRIPTION_PLAN_SIX_MONTH_SDK() -> str:
        return os.environ.get("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_SIX_MONTH_SDK") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_SUBSCRIPTION_PLAN_SIX_MONTH_SDK")
    
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_1() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_1") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_1")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_2() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_2") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_2")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_3() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_3") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_3")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_4() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_4") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_4")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_5() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_5") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_5")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_6() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_6") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_6")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_7() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_7") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_7")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_8() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_8") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_8")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_9() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_9") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_9")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_10() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_10") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_10")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_11() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_11") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_11")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_12() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_12") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_12")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_13() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_13") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_13")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_14() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_14") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_14")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_15() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_15") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_15")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_16() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_16") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_16")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_17() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_17") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_17")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_18() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_18") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_18")
    @staticmethod
    def CAFFE_BAZZAR_PURCHASE_PLAN_19() -> str:
        return os.environ.get("CAFFE_BAZZAR_PURCHASE_PLAN_19") or EnvirenmentVariable._raise_env_error("CAFFE_BAZZAR_PURCHASE_PLAN_19")
    
    @staticmethod
    def EMAILSMTPUSERNAME() -> str:
        return os.environ.get("EMAIL_SMTP_USERNAME") or EnvirenmentVariable._raise_env_error("EMAIL_SMTP_USERNAME")
    
    @staticmethod
    def EMAILSMTPAPPPASSWORD() -> str:
        return os.environ.get("EMAIL_SMTP_APP_PASSWORD") or EnvirenmentVariable._raise_env_error("EMAIL_SMTP_APP_PASSWORD")
    
    @staticmethod
    def EMAILSMTPHOST() -> str:
        return os.environ.get("EMAIL_SMTP_HOST") or EnvirenmentVariable._raise_env_error("EMAIL_SMTP_HOST")
    
    @staticmethod
    def EMAILSMTPPORT() -> str:
        return os.environ.get("EMAIL_SMTP_PORT") or EnvirenmentVariable._raise_env_error("EMAIL_SMTP_PORT")

    @staticmethod
    def _raise_env_error( var_name: str):
        raise EnvironmentError(f"Missing required environment variable: {var_name}")