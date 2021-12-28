import asyncio

async def fetch_data():
    print("fetching data")
    await asyncio.sleep(6)
    print("data returned...")
    return {"data":100}

async def counter():
    for i in range(1,11):
        print(i)
        await asyncio.sleep(1)

async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(counter())
    
    #data = await x
    #print(data)
    #await y
    
    print(x)
    print(y)
    
asyncio.run(main())