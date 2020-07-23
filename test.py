import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def test():
    print(f"tests called at {time.strftime('%X')}")
    task1 = asyncio.create_task(
        say_after(1, f"one seconds {time.strftime('%X')}")
    )
    task2 = asyncio.create_task(
        say_after(2, f"two seconds {time.strftime('%X')}")
    )

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"test finished at {time.strftime('%X')}")

asyncio.run(test())
