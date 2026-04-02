import asyncio
import time


async def eat():
    for i in range(6):
        print('正在吃饭...')
        await asyncio.sleep(0)


async def work():
    for i in range(6):
        print('正在做作业...')
        await asyncio.sleep(0)


async def main():
    start = time.time()
    await asyncio.gather(work(),eat())
    end = time.time()
    print(f'耗时:{end - start}')


if __name__ == '__main__':
    asyncio.run(main())