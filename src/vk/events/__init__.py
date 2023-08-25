import builtins
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Any, Tuple, Union, get_args, get_origin

from pydantic import BaseModel


def is_builtin_type(tp):
    return tp in vars(builtins).values() or get_origin(tp) in vars(builtins).values()


class AttributeValidationErrorType(str, Enum):
    MISSING = "MISSING"
    INCORRECT = "INCORRECT"


class AttributeValidationError(Exception):
    """Exception raised if there is no value when it is needed or if the type is incorrect
    """

    def __init__(
            self,
            error_type: AttributeValidationErrorType,
            *,
            key: str,
            value: Any = None,
            actual_type: Any = None,
            expected_type: Any = None,
            message: str = "Field error [type={type}, key={key}, value={value}, actual_type={actual_type}, expected_type={expected_type}]"
    ):
        """
        :param str key: field name
        :type key: str
        :param value: field value
        :type value: Any
        :param actual_type: field type
        :type actual_type: Any
        :param expected_type: expected field type
        :type expected_type: Any
        :param message: error text template
        :type message: str
        """

        self.message = message.format(type=error_type.value, key=key, value=value, actual_type=actual_type, expected_type=expected_type)
        super().__init__(self.message)


class ABCEvent(ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def pack(self):
        payload = {
            "prefix": self.__class__.__name__
        }

        for key, _type in self.__class__.__annotations__.items():
            value = self.kwargs.get(key, None)

            if value is None and not _type == Optional[_type]:
                raise AttributeValidationError(AttributeValidationErrorType.MISSING, key=key)

            if value is not None and not (
                    (is_builtin_type(_type) and type(value) == _type)
                    or (get_origin(_type) and type(value) in get_args(_type))
            ):
                raise AttributeValidationError(
                    AttributeValidationErrorType.INCORRECT,
                    key=key,
                    value=value,
                    actual_type=type(value),
                    expected_type=_type,
                )

            payload[key] = value

        return payload

    @classmethod  # TODO возвращает Callback кнопку с .pack(), Label, color
    def configure(cls):
        return NotImplemented

    @classmethod  # TODO фильтрует dict по хранящемуся в нём prefix, и, далее по кастомным ключам если prefix от ивента
    def filter(cls, **kwargs):
        return NotImplemented


class CustomEvent(ABCEvent):
    mew: Optional[int]


print(CustomEvent(mew=1).pack())
