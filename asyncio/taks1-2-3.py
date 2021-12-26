import asyncio
from asyncio.tasks import sleep

async def task1():
    print("send first Email")
    asyncio.create_task(task2())
    await asyncio.sleep(3)
    print("first Email reply")
    
async def task2():
    print("send second Email")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("second Email reply")
    
async def task3():
    print('send third email')
    await asyncio.sleep(1)
    print("third Email reply")
    
asyncio.run(task1())