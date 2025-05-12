from pydantic import AnyUrl


class AutoHttpUrl(AnyUrl):
    """
    URL type that prepends 'https://' if no scheme is provided.
    """
    allowed_schemes = {"http", "https"}

    @classmethod
    def __get_validators__(cls):
        yield cls._prep_value
        yield from super().__get_validators__()

    @classmethod
    def _prep_value(cls, value):
        if isinstance(value, str) and "://" not in value:
            return "https://" + value
        return value
