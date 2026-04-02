from jinja2.filters import do_groupby


class Animal(object):
    __name = '动物'#私有属性

    def __init__(self,color):
        self.__color = color#私有属性

    def __run(self):#私有函数
        print('动物跑起来')
        print(self.__name)#类的里面可以访问私有属性

    def say(self):
        print('动物喊叫')
        self.__run()
        print(self.__color)
        print(self.__name)
        self.__color = 'green'
        Animal.__name = '生物'
        print(self.__color)
        print(self.__name)


    def set_color(self,new_color):#通过一个set函数来修改私有属性
        self.__color = new_color

    def get_color(self):
        return self.__color




class Dog(Animal):
    pass

d = Dog('red')
d.say()
print('*'*60)
d.set_color('abc')
d.say()
print(d.get_color())