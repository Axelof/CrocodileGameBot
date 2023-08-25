import contextlib


class DotDict(dict):
    """dot.notation access to dictionary attributes"""

    def __init__(self, obj=None):
        if obj is None:
            obj = {}
        for key, value in obj.items():
            if isinstance(value, dict):
                obj[key] = DotDict(value)
        super().__init__(obj)

    __getattr__ = dict.get

    def __delattr__(self, item):
        with contextlib.suppress(KeyError):
            del self[item]

    def __setattr__(self, key: str, value):
        if isinstance(value, dict):
            self[key] = DotDict(value)
        else:
            self[key] = value
