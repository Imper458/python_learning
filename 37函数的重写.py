class Parent:

    def __init__(self,name):
        self.name = name
        print('parent的init函数被执行了')

    def say_hello(self):
        print(f'{self.name} says hello')
        print('parent的say_hello函数被执行了')

class Son(Parent):
    def __init__(self,name,age):
        super().__init__(name)#在子类中调用父类的init函数，重载
        self.age = age
        print('Son的init函数被执行了')

    def say_hello(self):
        print(f'{self.name} says helloworld')
        print('Son的say_hello函数被执行了')


s1 = Son('张三',32)
s1.say_hello()