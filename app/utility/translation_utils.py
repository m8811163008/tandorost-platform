import gettext

from data.common_data_model.language import Language

# from typing import List, Tuple

class TranslationManager:
    def __init__(self, default_language: Language = Language.ENGLISH, locales_dir: str = "app/locales"):
        self.default_language = default_language
        self.locales_dir = locales_dir
        self.translation: gettext.NullTranslations | None = None
        self.supported_languages = [Language.ENGLISH, Language.PERSIAN]  # List of supported languages
        self.set_language(default_language)

    def set_language_from_header(self, accept_language: str):
        """Set the language based on the Accept-Language header."""
        language = parse_accept_language(accept_language, self.supported_languages)
        self.set_language(language)

    def set_language(self, language: str):
        """Set the current language for translations."""
        parsed_language = parse_accept_language(language, self.supported_languages)
        self.translation = gettext.translation(
            "messages",
            localedir=self.locales_dir,
            languages=[parsed_language.value],
            fallback=True,
        )
        self.current_language = language
        self.translation.install()

    def gettext(self, message: str) -> str:
        """Get the translated message."""
        assert self.translation is not None
        return self.translation.gettext(message=message)


# Utility function to parse Accept-Language header
def parse_accept_language(header: str, supported_languages: list[Language]) -> Language:
    languages : list[tuple[str,float]]= []
    for lang in header.split(","):
        parts = lang.split(";q=")
        language = parts[0].strip()
        quality = float(parts[1]) if len(parts) > 1 else 1.0
        languages.append((language, quality))

    # Sort languages by quality value (q) in descending order
    languages.sort(key=lambda x: x[1], reverse=True)

    # Find the first supported language
    for language, _ in languages:
        if language in supported_languages:
            return Language(language)

    # Fallback to the default language
    return Language.ENGLISH  # Default language


# Create a global instance of the TranslationManager
translation_manager = TranslationManager()

