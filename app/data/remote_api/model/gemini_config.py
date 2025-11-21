from enum import StrEnum
from pydantic import BaseModel

class AIModel(StrEnum):
    # TODO get list of models from gemini
    GEMINI3PREVIEW = 'gemini-3-pro-preview'
    GEMINI25PRO = 'gemini-2.5-pro'
    GEMINI25FLASH = 'gemini-2.5-flash'
    GEMINI2FLASHLIGHT = 'gemini-2.5-flash-lite'

class GeminiConfig(BaseModel):
    api_key : str
    models : list[AIModel] = [
        AIModel.GEMINI25FLASH,
        AIModel.GEMINI2FLASHLIGHT,
        AIModel.GEMINI3PREVIEW,
        AIModel.GEMINI25PRO,
    ]
