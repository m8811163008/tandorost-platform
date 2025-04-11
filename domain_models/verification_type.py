from enum import Enum


class VerificationType(Enum):
    REGISTER = 'register'
    FORGOT_PASSWORD = 'forgot_password'

    def is_register(self) -> bool:
        return self == VerificationType.REGISTER