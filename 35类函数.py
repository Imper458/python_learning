class Person:

    category = '人类'

    def __init__(self, name, age):#成员函数
        self.name = name
        self.age = age


    def eat(self):#成员函数
        print(f'{self.name}正在吃饭')

    #类函数
    @classmethod
    def run2(cls,other,num=100):
        print(f'这个是类函数,other是{other}')

    #静态函数
    @staticmethod
    def run1(pp1):
        print(f'这个是静态函数{pp1}')

p1 = Person('张三',16)
p1.eat()
p1.run2(5)
print(Person.category)
p1.run1(2)