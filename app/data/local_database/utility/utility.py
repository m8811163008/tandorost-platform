from enum import StrEnum, auto
import re


class UsernameType(StrEnum):
    EMAIL = auto()
    PHONENUMBER = auto()
    INVALID = auto()

def username_type(username: str) -> UsernameType:
    if re.match(r'^09\d{9}$', username):
        return UsernameType.PHONENUMBER
    elif re.match(r'^[^@]+@[^@]+\.[^@]+$', username):
        return UsernameType.EMAIL
    else:
        return UsernameType.INVALID