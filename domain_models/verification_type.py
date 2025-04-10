from enum import Enum


class VerificationType(Enum):
    REGISTER = 'REGISTER'
    FORGOT_PASSWORD = 'FORGOT_PASSWORD'

    def is_register(self) -> bool:
        return self == VerificationType.REGISTER