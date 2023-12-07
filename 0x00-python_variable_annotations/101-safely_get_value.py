#!/usr/bin/env python3
"""adding type annotations to the function"""

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """annotations of the function"""
    if key in dct:
        return dct[key]
    else:
        return default
