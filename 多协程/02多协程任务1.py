import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭...')
        await asyncio.sleep(0.5)


async def work():
    for i in range(6):
        print('正在做作业...')
        await asyncio.sleep(0.5)


async def main():
    #协程切换,但是是同步的
    await eat()
    await work()


if __name__ == '__main__':
    asyncio.run(main())