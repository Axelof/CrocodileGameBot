from typing import Any

from aiogram.filters.callback_data import CallbackData


class PydanticCallbackData(CallbackData, prefix='pydantic_callback_data'):
    def __init_subclass__(cls, **kwargs):
        if 'prefix' not in kwargs:
            kwargs['prefix'] = cls.__name__

        super().__init_subclass__(**kwargs)

    def _encode_value(self, key: str, value: Any) -> str:
        serialized = self.Config.json_dumps(value, default=self.__json_encoder__)
        deserialized = self.Config.json_loads(serialized)
        if deserialized is None:
            return ''

        return str(deserialized)
