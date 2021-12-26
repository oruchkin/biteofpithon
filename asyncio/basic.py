import asyncio

async def send_email():
    print("hello")
    await asyncio.sleep(2)
    print("hey2sec")
    
#send_email()
asyncio.run(send_email())