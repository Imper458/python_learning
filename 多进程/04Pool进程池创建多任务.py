import time
from multiprocessing import Process, Pool


#吃饭任务
def eat(name):
    for i in range(6):
        print(f'{name}正在吃饭...')
        time.sleep(0.3)



#做作业任务
def work():
    for i in range(6):
        print('正在做作业...')
        time.sleep(0.3)

#打游戏任务
def game():
    for i in range(6):
        print('正在打游戏...')
        time.sleep(0.3)

if __name__ == '__main__':
    process_pool = Pool(2)

    #apply是阻塞函数
    # process_pool.apply(eat,args=('张三',))#从主进程中请求一个子进程去执行eat
    # process_pool.apply(work)


    #async：异步调用（非阻塞）
    process_pool.apply_async(eat, args=('张三',))
    process_pool.apply_async(work)
    process_pool.apply_async(game)

    #close表示进程池关闭，进程池不再接受新的进程的请求
    process_pool.close()
    # process_pool.apply_async(game)#报错

    #采用进程池的异步调用，一定要手动调用join
    process_pool.join()