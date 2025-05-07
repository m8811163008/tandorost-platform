from enum import Enum
from typing import Any


class ResponseStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"


class ApiResponse:
    def __init__(
        self,
        status: ResponseStatus,
        message: str | None,
        data: str | None = None,
        error_detail: str | None = None,
    ):
        # Ensure data and error cannot coexist
        assert not (data is not None and error_detail is not None), (
            "ApiResponse cannot have both 'data' and 'error' at the same time."
        )
        self.status = status
        self.message = message
        self.data = data
        self.error_detail = error_detail

    @classmethod
    def success(cls, message: str | None = None, data: Any = None) -> "ApiResponse":
        """Named constructor for success responses."""
        return cls(status=ResponseStatus.SUCCESS, message=message, data=data)

    @classmethod
    def error(cls, message: str, error_detail: str | None = None) -> "ApiResponse":
        """Named constructor for error responses."""
        return cls(
            status=ResponseStatus.ERROR,
            message=message,
            error_detail=error_detail,
        )

    def to_dict(self) -> dict[Any, Any]:
        """Convert the response to a dictionary."""
        response: dict[str, Any] = {
            "status": self.status.value,
            "message": self.message,
        }
        if self.data is not None:
            response["data"] = self.data
        if self.error_detail is not None:
            response["error_detail"] = self.error_detail,
        return response