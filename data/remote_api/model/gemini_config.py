from enum import StrEnum
from pydantic import BaseModel

class AIModel(StrEnum):
    # TODO get list of models from gemini
    GEMINI25PREVIEW = 'gemini-2.5-flash'
    GEMINI25PRO = 'gemini-2.5-pro'
    GEMINI2FLASH = 'gemini-2.5-flash-lite-preview-06-17'
    GEMINI2FLASHLITE = 'gemini-2.0-flash'

class GeminiConfig(BaseModel):
    api_key : str
    models : list[AIModel] = [
        AIModel.GEMINI25PREVIEW,
        AIModel.GEMINI25PRO,
        AIModel.GEMINI2FLASH,
        AIModel.GEMINI2FLASHLITE
    ]
