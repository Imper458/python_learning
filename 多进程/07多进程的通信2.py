import time
from multiprocessing import Process, Pool, Queue, Pipe

my_list = []

#吃饭任务
def add_data(pi: Pipe):
    for i in range(6):
        my_list.append(i)
        pi.send(f'数据{i}')
        time.sleep(0.1)




#做作业任务
def read_data(pi: Pipe):
    while True:
        #recv()是阻塞函数
        value = pi.recv()
        print(value)
        time.sleep(0.4)


if __name__ == '__main__':
    #创建一个管道,需要两个端点
    send_pi , recv_pi = Pipe()

    p1 = Process(target=add_data, args=(send_pi,))#往队列中存放数据的进程
    p2 = Process(target=read_data, args=(recv_pi,))#从队列中获取数据的进程

    p1.start()

    p2.start()

