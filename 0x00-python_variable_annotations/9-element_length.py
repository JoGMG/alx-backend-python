#!/usr/bin/env python3
"""
A type-annotated version of Task 9's function.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple containing the items and length of a sequence.

    Argument:
        - `lst`: a sequence
    """
    return [(i, len(i)) for i in lst]
