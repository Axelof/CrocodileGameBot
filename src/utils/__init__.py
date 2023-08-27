import builtins
from typing import get_origin


def is_builtin_type(tp):
    return tp in vars(builtins).values() or get_origin(tp) in vars(builtins).values()


def get_class_variables(cls: object):
    return {key: value for key, value in vars(cls).items() if not key.startswith("__")}