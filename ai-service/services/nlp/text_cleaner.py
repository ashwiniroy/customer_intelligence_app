import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

        text = text.strip()

        text = re.sub(r"\s+", " ", text)

        return text