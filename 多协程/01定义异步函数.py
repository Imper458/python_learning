import asyncio
import time


# 普通函数
def hello(msg: str):
    print(f'hello{msg}')


# 定义一个异步函数
async def test1():
    print('hello')
    # 挂起当前的协程，等待1秒钟
    # 当协程挂起的时候，可以去执行卡的协程（异步任务）
    await asyncio.sleep(1)
    time.sleep(1)  # 不会进行协程的切换，只会让当前线程挂起，并且等待1秒
    print('world')


hello('laoxiao')
# #创建了一个协程，但是协程还没开始
# coroutine = test1()
# print(coroutine)


# 启动协程
b = test1()
asyncio.run(b)
