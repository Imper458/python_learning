# 3.观察者模式
from abc import ABC, abstractmethod


# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


# 具体观察者
class EmailSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} 收到邮件通知：{message}")


class SMSSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} 收到短信通知：{message}")


# 主题（被观察者）
class NewsPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber: Observer):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Observer):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, message: str):
        for subscriber in self._subscribers:
            subscriber.update(message)


# 使用示例
publisher = NewsPublisher()

# 创建订阅者
alice = EmailSubscriber("Alice")
bob = SMSSubscriber("Bob")

# 订阅新闻
publisher.subscribe(alice)
publisher.subscribe(bob)

# 发布新闻
publisher.notify_subscribers("Python 3.12 发布了！")

# 取消订阅
publisher.unsubscribe(alice)
publisher.notify_subscribers("这是只有 Bob 能看到的通知")
#总结一下，这个案例就是把alice和bob对象放到私有属性_subscribers列表中，然后在notify_subscribers方法分别调用这两个对象的update方法。remove后就没有了
print('*'*50)
