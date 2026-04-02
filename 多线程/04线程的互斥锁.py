from threading import Thread,Lock

g_num = 0

lock = Lock()#创建锁

#需求：采用两个线程分别对g_num累加100万次

def su_num1():
    lock.acquire()#阻塞
    for i in range(1000000):
        global g_num
        g_num += 1
    lock.release()
    print(f'线程1累加之后的结果{g_num}')


def su_num2():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    lock.release()
    print(f'线程2累加之后的结果{g_num}')


if __name__ == '__main__':
    t1 = Thread(target=su_num1)
    t2 = Thread(target=su_num2)

    t1.start()
    # t1.join()#主线程在这阻塞，两个线程的同步运行

    t2.start()