import time
from multiprocessing import Process, Pool, Queue

my_list = []

#吃饭任务
def add_data(q: Queue):
    for i in range(6):
        my_list.append(i)
        q.put(f'数据{i}')
        time.sleep(0.1)




#做作业任务
def read_data(q: Queue):
    while True:
        #get()是阻塞函数，get只从队列中获取一个值，并且这个值将从队列中删除
        value = q.get()
        print(value)
        time.sleep(0.4)


if __name__ == '__main__':
    q = Queue(100)
    p1 = Process(target=add_data, args=(q,))#往队列中存放数据的进程
    p2 = Process(target=read_data, args=(q,))#从队列中获取数据的进程

    p1.start()

    p2.start()

