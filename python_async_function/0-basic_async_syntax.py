#!/usr/bin/env python3

"""
Asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""

import asyncio
import random
from typing import Union

async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (Union[int, float]): The maximum delay to wait for.
    
    Returns:
        float: The random delay waited.
    """
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay
