#传入不同的对象，产生不同的结果

class Animal:
   def say(self):
       pass

class Dog(Animal):
    def say(self):
        print('旺旺')


class Cat(Animal):
    def say(self):
        print('喵喵')

def test(obj: Animal):
    obj.say()


d = Dog()
c = Cat()

test(d)
test(c)