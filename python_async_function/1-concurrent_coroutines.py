#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''

import asyncio
from typing import List
from random import uniform
from asyncio import sleep
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """list of all the delays"""
    spawn_ls = []
    delay_ls = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        spawn_ls.append(delayed_task)

    for spawn in spawn_ls:
        await spawn

    return sorted(delay_ls)

async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

if __name__ == "__main__":
    asyncio.run(main())
