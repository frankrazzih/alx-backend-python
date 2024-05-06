#!/usr/bin/env python3
'''using random library'''
import asyncio
import random
async def  wait_random(max_delay=10):
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time