#!/usr/bin/env python3
""" From the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    ''' Returns asyncio.Task object '''
    return asyncio.create_task(wait_random(max_delay))
