class Animal:
    name = "动物"

    def say(self):
        print('动物的叫声')

class Dog(Animal):#子类只继承一个父类:单继承

    def see_home(self):
        print('狗可以看家')



d = Dog()
d.say()
print(d.name)
d.see_home()

# 子类的对象 是子类类型，同时也是父类类型
print(type(d))
print(isinstance(d, Animal))

print(issubclass(Animal,Dog))