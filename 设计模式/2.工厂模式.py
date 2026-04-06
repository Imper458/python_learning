# 2.工厂模式：基类不实现方法，只在子类实现
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self,message:str):
        pass
class EmailNotification(Notification):
    def send(self,message:str):
        print(f"发送邮件：{message}")

class SMSNotification(Notification):
    def send(self,message:str):
        print(f"发送短信：{message}")

# 工厂类
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("不支持的通知类型")

# 使用示例
email = NotificationFactory.create_notification("email")
sms = NotificationFactory.create_notification("sms")

email.send("您的订单已发货")
sms.send("验证码：123456")
print('*'*50)

#案例2
from abc import ABC, abstractmethod
#抽象产品A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

#抽象产品B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# 具体产品 A1
class WindowsButton(Button):
    def paint(self):
        return "渲染 Windows 按钮"

# 具体产品 A2
class MacButton(Button):
    def paint(self):
        return "渲染 Mac 按钮"

# 具体产品 B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        return "渲染 Windows 复选框"

# 具体产品 B2
class MacCheckbox(Checkbox):
    def paint(self):
        return "渲染 Mac 复选框"


# 抽象工厂
class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass


# 具体工厂 1
class WindowsFactory(GUIFactory):
    def createButton(self) -> Button:
        return WindowsButton()

    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()


# 具体工厂 2
class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()


# 客户端代码
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def createUI(self):
        self.button = self.factory.createButton()
        self.checkbox = self.factory.createCheckbox()

    def paint(self):
        result = []
        if self.button:
            result.append(self.button.paint())
        if self.checkbox:
            result.append(self.checkbox.paint())
        return "\n".join(result)


# 使用示例
def test_abstract_factory():
    # 根据系统类型选择工厂
    system_type = "windows"  # 可以自动检测或从配置读取

    if system_type == "windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()

    app = Application(factory)
    app.createUI()
    print(app.paint())


if __name__ == "__main__":
    test_abstract_factory()