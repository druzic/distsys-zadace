import asyncio
import os

async def afun1(lista):
    await asyncio.sleep(0.2)
    return [{"naziv datoteke":x , "file size": os.path.getsize(x)} for x in lista]

def fun2(lista):
    for x in lista:
        f = open(x,"w")
        for y in range(1,10000):
            f.write(str(y))
        f.close



async def main():
    lista = ["datoteka1", "datoteka2", "datoteka3"]
    for x in lista:
        open(x, "w")

    ispis = asyncio.create_task(afun1(lista))

    fun2(lista)
    await ispis
    print(ispis.result())





if __name__ == "__main__":
    asyncio.run(main())