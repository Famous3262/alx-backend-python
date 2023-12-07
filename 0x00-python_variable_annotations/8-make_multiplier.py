#!/usr/bin/env python3
""" A type-annotated function that takes a float as argument
and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
