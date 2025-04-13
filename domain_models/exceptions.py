
class UsernameAlreadyInUse(Exception):
    pass

class UsernameNotRegisteredYet(Exception):
    pass

class UsernameIsInactive(Exception):
    pass

class InvalidVerificationCode(Exception):
    pass

class InvalidPassword(Exception):
    pass




class VerifiationCodeRequestReachedLimit(Exception):
    def __init__(self, seconds_left: int) -> None:
        self.seconds_left = seconds_left