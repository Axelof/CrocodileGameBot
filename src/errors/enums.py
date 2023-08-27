from enum import auto

from src.enums import AutoName


class AttributeValidationErrorType(AutoName):
    MISSING = auto()
    INCORRECT = auto()