#!/usr/bin/env python3
"""
Take the code from `wait_n` in `1-concurrent_coroutines` and alter it
into a new function `task_wait_n`. The code is nearly identical to
`wait_n` except `task_wait_random` is being called.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Awaits `task_wait_random` results `n` times in a list, sorts and
    returns them.

    Arguments:
        - `n`: number of times to run `task_wait_random`
        - `max_delay`: maximum delay time
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
