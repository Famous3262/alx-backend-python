#!/usr/bin/env python3
"""A coroutine called async_comprehension that takes no argument.
Return the 10 random numbers collected using
an async comprehensing over async_generator
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return the 10 random numbers"""
    return [result async for result in async_generator()]
