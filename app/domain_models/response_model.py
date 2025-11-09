
from pydantic import BaseModel



class ErrorResponse(BaseModel):
    error_detail: str | None 
    message: str | None = None