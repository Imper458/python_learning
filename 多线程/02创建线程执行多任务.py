from threading import Thread
import time

class EatThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'线程{self.name}：正在吃饭...')
            time.sleep(0.3)


class WorkThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(6):
            print(f'线程{self.name}：正在做作业...')
            time.sleep(0.3)

if __name__ == '__main__':
    p1 = EatThread('process-1')
    p2 = WorkThread('process-2')

    p1.start()
    p2.start()