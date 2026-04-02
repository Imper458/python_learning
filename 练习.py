class Parent:
    def mymethod(self,x):
        print("调用父类方法")
        y = x+1
        print('y的值是：',y)

class Child(Parent):
    def mymethod(self,x):
        print("调用子类方法")
        super(Child,self).mymethod(x)


a = Parent()#实例化
a.mymethod(1)

b = Child()
b.mymethod(2)

super(Child,b).mymethod(5)

c = Child()
c.mymethod(3)



class FooParent(object):
    def __init__(self):
        self.parent = 'I m the parent.'
        print('parent')

    def bar(self,message):
        print('%s from Parent' % message)

class FooChild(FooParent):
    def __init__(self):
        super(FooChild,self).__init__()
        print('child bar function')
        print(self.parent)

if __name__ == '__main__':
    foo = FooChild()#到这里就执行FooChild的__init__，然后因为有super就去执行父类的__init__，执行完父类以后又回来继续执行 print('child bar function')   print(self.parent)
    foo.bar('hello')


class Solution1:
    def twoSum(self, nums, target) :
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
p = Solution1()
twosum = p.twoSum(nums=[2, 7, 11, 15], target=17)
print(twosum)














