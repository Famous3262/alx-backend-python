#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no argument.
Return the 10 random numbers collected using
an async comprehensing over async_generator
"""


from typing import List
from importlib import import_module as using
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    rand_numbers = [num async for num in async_generator()]
    return rand_numbers
