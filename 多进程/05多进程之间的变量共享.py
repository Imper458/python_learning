import time
from multiprocessing import Process, Pool

my_list = []

#吃饭任务
def add_data():
    for i in range(6):
        my_list.append(i)
        print(my_list)
        time.sleep(0.3)
    print(my_list)



#做作业任务
def read_data():
    print(my_list)


if __name__ == '__main__':
    p1 = Process(target=add_data)
    p2 = Process(target=read_data)

    p1.start()
    p1.join()
    p2.start()