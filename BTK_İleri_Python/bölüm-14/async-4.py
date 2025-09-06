import asyncio
import time

async def fetch_data(id,delay):
    print("veri alınıyor...id:",id)
    await asyncio.sleep(delay)
    print("veri alındı... id:",id)
    return {"id":id,"data":"bazı veriler"}

async def main():
    print("start")
    results=await asyncio.gather(fetch_data(1,2),fetch_data(2,3),fetch_data(3,1))

    for result in results:
        print(result)
        
    print("end")
t=time.time()
asyncio.run(main())
print(time.time()-t)
