#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
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
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
