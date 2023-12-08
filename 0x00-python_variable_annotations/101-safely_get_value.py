#!/usr/bin/env python3
"""
A type-annotated version of Task 11's function.
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
R = Union[Any, T]
Deftype = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Deftype = None) -> R:
    """
    Returns the value of a key in a dictionay if it exists, else
    returns default.

    Arguments:
        - `dct`: a mapping type data structure (dict)
        - `key`: any value
        - `default`: a string 'T' or None type value
    """
    if key in dct:
        return dct[key]
    else:
        return default
