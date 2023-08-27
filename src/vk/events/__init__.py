from abc import ABC
from typing import get_args, get_origin, Optional, Any, final

from errors.attributes import AttributeValidationError
from errors.enums import AttributeValidationErrorType
from utils import is_builtin_type, get_class_variables

from vkbottle import Callback


class BaseEvent(ABC):
    def __init__(self, **kwargs):
        if self.__class__.__name__ == BaseEvent.__name__:
            raise TypeError("BaseEvent cannot be instantiated directly")

        self.prefix = self.__class__.__name__
        self.kwargs = kwargs

        self.payload = self.pack()

    @final
    def pack(self) -> dict[str, Any]:
        payload = {
            "prefix": self.prefix
        }

        for key, _type in self.__class__.__annotations__.items():
            value = self.kwargs.get(key, None) or get_class_variables(self.__class__).get(key, None)

            if value is None and _type not in [_type | None, Optional[_type]]:  # support new syntax
                raise AttributeValidationError(AttributeValidationErrorType.MISSING, key=key, expected_type=_type)

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

    @final
    def button(self, label: str) -> Callback:
        """

        :param label: Button Text
        :return: Callback button with completed values
        """

        return Callback(
            label=label,
            payload=self.payload
        )

    @classmethod  # TODO фильтрует dict по хранящемуся в нём prefix, и, далее по кастомным ключам если prefix от ивента
    @final
    def filter(cls, **kwargs):
        return NotImplemented
