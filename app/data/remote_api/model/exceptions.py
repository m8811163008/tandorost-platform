class NetworkConnectionError(Exception):
    """Raised when there is a network connection issue."""
    pass


class InvalidArgumentError(Exception):
    """Raised when the request body is malformed."""
    def __init__(self, message: str = "The request body is malformed. Check the API reference for request format, examples, and supported versions."):
        super().__init__(message)


class FailedPreconditionError(Exception):
    """Raised when the Gemini API free tier is not available in the user's country."""
    def __init__(self, message: str="Gemini API free tier is not available in your country. Please enable billing on your project in Google AI Studio."):
        super().__init__(message)


class PermissionDeniedError(Exception):
    """Raised when the API key doesn't have the required permissions."""
    def __init__(self, message: str="Your API key doesn't have the required permissions. Check that your API key is set and has the right access."):
        super().__init__(message)


class NotFoundError(Exception):
    """Raised when the requested resource wasn't found."""
    def __init__(self, message: str="The requested resource wasn't found. Check if all parameters in your request are valid for your API version."):
        super().__init__(message)


class ResourceExhaustedError(Exception):
    """Raised when the rate limit is exceeded."""
    def __init__(self, message: str="You've exceeded the rate limit. Ensure you're within the model's rate limit or request a quota increase if needed."):
        super().__init__(message)


class InternalError(Exception):
    """Raised when an unexpected error occurs on Google's side."""
    def __init__(self, message: str="An unexpected error occurred on Google's side. Reduce your input context or retry your request."):
        super().__init__(message)


class ServiceUnavailableError(Exception):
    """Raised when the service is temporarily overloaded or down."""
    def __init__(self, message: str="The service may be temporarily overloaded or down. Retry your request or switch to another model."):
        super().__init__(message)


class DeadlineExceededError(Exception):
    """Raised when the service is unable to finish processing within the deadline."""
    def __init__(self, message: str="The service is unable to finish processing within the deadline. Set a larger 'timeout' in your client request."):
        super().__init__(message)

class ParameterError(Exception):
    """Raised when the response contains a null parameter and AI models could not complete the request."""
    def __init__(self, message: str="The response contains a null parameter, and the AI models could not complete the request. Verify your input and try again."):
        super().__init__(message)
        
class VerifyRejection(Exception):
    """Raised when the response contains a null parameter and AI models could not complete the request."""
    def __init__(self, message: str="The verification response is False"):
        super().__init__(message)