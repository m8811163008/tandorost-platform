class DocumentNotFound(Exception):
    pass

class UserBioDataValidationError(Exception):
    def __init__(self,detail : str, *args: object) -> None:
        self.detail = detail
        super().__init__(*args)