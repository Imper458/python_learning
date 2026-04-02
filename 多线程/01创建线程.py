import time
from threading import Thread


#采用两个线程，累加1，加5亿次

def add(n):
    '''
    把1累加多少次
    :param n:
    :return:
    '''
    sum = 0
    while sum<n:
        sum+=1
    print(f'当前线程加了{sum}次')

if __name__ == '__main__':
     start = time.time()
     n = 500000000

    #加了daemon就是把子线程变成守护线程。也就是说，当主线程结束以后，所有的守护线程也强行中断
     t1 = Thread(target=add, args=(n/2,),daemon=True)
     t2 = Thread(target=add, args=(n/2,),daemon=True)

     #守护线程也可以这样创建
     # t1.daemon = True

     t1.start()
     t2.start()

     # t1.join()
     # t2.join()
     #

     #单线程
     # add(n)



     end = time.time()
     print(f'运行的时间为：{end-start}')


#在这个案例中，单线程比多线程快，因为多线程抢夺GIL锁耗时多
#但这个项目比较特殊，因为没有IO操作。如果以后IO操作多的话多线程会更快