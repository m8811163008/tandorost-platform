
from datetime import datetime
from enum import StrEnum
from pydantic import   BaseModel, Field, ConfigDict, computed_field

class Currency(StrEnum):
    IRRIAL = 'ir_rial'
