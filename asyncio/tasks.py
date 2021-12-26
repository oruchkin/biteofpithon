import asyncio

async def task1():
    await task2()
    print("task1")

async def task2():
    await task3()
    print("task2")


async def task3():
    print("task3")


asyncio.run(task1())