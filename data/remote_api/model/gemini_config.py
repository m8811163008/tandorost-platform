from enum import StrEnum
from pydantic import BaseModel

class AIModel(StrEnum):
    GEMINI25PREVIEW = 'gemini-2.5-flash-preview-04-17'
    GEMINI25PRO = 'gemini-2.5-pro-preview-03-25'
    GEMINI2FLASH = 'gemini-2.0-flash'
    GEMINI2FLASHLITE = 'gemini-2.0-flash-lite'

class GeminiConfig(BaseModel):
    api_key : str
    models : list[AIModel] = [
        AIModel.GEMINI25PREVIEW,
        AIModel.GEMINI25PRO,
        AIModel.GEMINI2FLASH,
        AIModel.GEMINI2FLASHLITE
    ]
