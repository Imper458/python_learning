class Parent():
    def __init__(self,name,*args,**kwargs):
        self.name = name
        print('parent的init函数被执行了')

    def text(self):
        print('parent的text函数被执行了')

class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        self.age = age
        super().__init__(name,*args,**kwargs)
        print('Son1的init函数被执行了')

    def text(self):
        print('Son1的text函数被执行了')

class Son2(Parent):
    def __init__(self, name, sex, *args, **kwargs):
        self.sex = sex
        super().__init__(name, *args, **kwargs)
        print('Son2的init函数被执行了')

    def text(self):
        print('Son2的text函数被执行了')


class GrandSon(Son1,Son2):#多继承
    def __init__(self,name,age,sex,*args,**kwargs):
        super().__init__(name,age,sex)
        print('GrandSon的init函数执行了')


print(f'mro序列是:{GrandSon.__mro__}')
gs = GrandSon('zhangsan',34,'男')
gs.text()


class Son3(Parent):
    def __init__(self, msg, *args, **kwargs):
        self.msg = msg
        super().__init__(self, msg, *args, **kwargs)
        print('Son3的init函数被执行了')

    def text(self):
        print('Son3的text函数被执行了')


class GrandGrandSon(GrandSon,Son3):#多继承
    def __init__(self,name,age,sex,msg,*args,**kwargs):
        super().__init__(name,age,sex)
        print('GrandGrandSon的init函数执行了')

print(f'mro序列是:{GrandGrandSon.__mro__}')
ggs = GrandGrandSon('zjsj',3455,'女','aa')
ggs.text()