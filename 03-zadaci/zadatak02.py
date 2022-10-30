import asyncio
import numpy as np
import psutil


async def afunc1():
    for x in range(10):
        np.random.normal(size=(1000000))
        await asyncio.sleep(0.9)

async def afunc2():
    return psutil.cpu_percent(10)

async def main():
    asyncio.create_task(afunc1())
    ispis = await afunc2()
    print("Iskorištenost CPU u 10 sekundi iznosi : ", ispis)


if __name__ == "__main__":
    asyncio.run(main())