#!/usr/bin/env python3
"""Write a coroutine called async_generator
   that takes no arguments."""

import asyncio
import random

async def async_generator():
    """Coroutine that yields random numbers after waiting asynchronously for 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
