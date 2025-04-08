class UsernameAlreadyInUse(Exception):
    def __init__(self):
        self.detail = 'Username already in use'
        