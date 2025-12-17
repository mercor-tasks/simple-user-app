from .exceptions import BadRequestError


def validate_empty_string(s: str, paramName: str):
    if len(s.strip()) == 0:
        raise BadRequestError(f"{paramName} is empty")
