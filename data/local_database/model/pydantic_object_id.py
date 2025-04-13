from typing import Any, Callable
from typing_extensions import Annotated
from bson import ObjectId as _ObjectId
from pydantic_core import core_schema
from pydantic.functional_serializers import PlainSerializer

class _ObjectIdPydanticAnnotation:
    # Based on https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types.

    @classmethod
    def __get_pydantic_core_schema__(
        # Generate a Pydantic core schema for the custom `_ObjectId` type.
        # This method is used to define how the `_ObjectId` type should be validated
        # and serialized when used with Pydantic models.
        # Args:
        #     cls: The class on which this method is defined.
        #     _source_type (Any): The source type for schema generation.
        #     _handler (Callable[[Any], core_schema.CoreSchema]): A handler function
        #         for generating core schemas.
        # Returns:
        #     core_schema.CoreSchema: A Pydantic core schema that validates and
        #     serializes the `_ObjectId` type.
        # The schema performs the following:
        #     1. Checks if the input is an instance of `_ObjectId`.
        #     2. If not, validates the input by attempting to create an `_ObjectId`
        #        instance from a string.
        #     3. Serializes the `_ObjectId` instance to a string representation.
        
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(input_value: str) -> _ObjectId:
            return _ObjectId(input_value)

        return core_schema.union_schema(
            [
                # check if it's an instance first before doing any further work
                core_schema.is_instance_schema(_ObjectId),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ],
            serialization=core_schema.to_string_ser_schema(),
        )

def decode_object_id(id: _ObjectId):
    """
    Converts an ObjectId instance to its string representation.

    Args:
        id (_ObjectId): The ObjectId instance to be converted.

    Returns:
        str: The string representation of the given ObjectId.
    """
    return str(id)

ObjectId = Annotated[
    _ObjectId, _ObjectIdPydanticAnnotation,
    PlainSerializer(decode_object_id, return_type=str)
]