
class UsernameAlreadyInUse(Exception):
    def __init__(self):
        self.detail = 'Username already in use'
class ObjectNotFound(Exception):
    def __init__(self):
        self.detail = 'Object not found'
class NetworkConnectionError(Exception):
    def __init__(self):
        self.detail = 'Could not create connection to sms panel'
        #TODO use l10n
