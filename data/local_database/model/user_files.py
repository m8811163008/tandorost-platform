
from datetime import datetime
from enum import StrEnum
from pydantic import BaseModel, Field,ConfigDict


class GallaryTag(Str):
    DEFAULT = 'default'
    PROFILE_IMAGE = 'profile_image'
    CERTIFICATE = 'certificate'

class ProcessingStatus(StrEnum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    ARCHIVED = 'archived'

class ImageRejectionReason(StrEnum):
    """
    Common reasons why an image might be rejected in a fitness application
    or according to software industry best practices.
    """
    POOR_QUALITY = "poor_quality"
    INAPPROPRIATE_CONTENT = "inappropriate_content"
    IRRELEVANT_CONTENT = "irrelevant_content"
    CROPPED_OR_OBSTRUCTED = "cropped_or_obstructed"
    POOR_LIGHTING = "poor_lighting"
    UNSAFE_ACTIVITY = "unsafe_activity"
    LACK_OF_CONSENT = "lack_of_consent"
    VIOLATES_GUIDELINES = "violates_guidelines"
    FILE_FORMAT_UNSUPPORTED = "file_format_unsupported"
    FILE_SIZE_TOO_LARGE = "file_size_too_large"
    WATERMARK_OR_LOGO = "watermark_or_logo"
    MISLEADING_OR_FALSE = "misleading_or_false"
    OTHER_REJECTION_REASON = "other_rejection_reason"



class FileData(BaseModel):
    id : str | None = Field(alias="_id", default=None)
    user_id : str
    tag : GallaryTag
    file_name:str
    file_size: int
    upload_date: datetime
    content_type: str
    file_upload_path: str
    # TODO implement admin panel for files processing status
    processing_status: ProcessingStatus = ProcessingStatus.APPROVED
    reject_processing_status_desc : ImageRejectionReason | None = None
    model_config = ConfigDict(use_enum_values=True,)







