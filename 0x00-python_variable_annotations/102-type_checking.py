#!/usr/bin/env python3
"""
Validating and applying necessary changes to Task 12's function.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns multiple copies of the items in lst
    based on the value of factor.

    Arguments:
        - `lst`: a tuple
        - `factor`: an integer with default value 2
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)