#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Use the random module"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return (delay)
