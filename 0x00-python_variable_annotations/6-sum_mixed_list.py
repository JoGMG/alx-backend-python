#!/usr/bin/env python3
"""
A type-annotated function `sum_mixed_list` which takes a list
`mxd_lst` of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of integer and float type numbers in a list as a float.

    Argument:
        - `mxd_lst`: a list of int and float type numbers
    """
    return float(sum(mxd_lst))
