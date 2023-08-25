import inspect
from typing import Callable, Any, Dict


def filter_kwargs(thing_with_kwargs: Callable, **kwargs) -> Dict[str, Any]:
    signature = inspect.signature(thing_with_kwargs)
    return {
        key: kwargs[key]
        for key in [
            parameter.name
            for parameter in signature.parameters.values()
            if parameter.kind in {inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY}
        ]
        if key in kwargs
    }
