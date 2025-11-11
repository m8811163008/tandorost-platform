from fastapi import  Header
from utility.translation_utils import translation_manager

async def get_accept_language(accept_language: str = Header(default="en")):
        if translation_manager.current_language != accept_language:
            translation_manager.set_language(accept_language)