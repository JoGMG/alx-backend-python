#!/usr/bin/env python3
"""
A type-annotated version of Task 10's function.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, else
    returns None.

    Argument:
        - `lst`: a sequence
    """
    if lst:
        return lst[0]
    else:
        return None
