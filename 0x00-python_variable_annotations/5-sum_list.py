#!/usr/bin/env python3
"""
A type-annotated function `sum_list` which takes a list `input_list`
of floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of float type numbers in a list as float.

    Argument:
        - `input_list`: a list of float type numbers
    """
    return float(sum(input_list))
