"""
把函数作为参数传入，或者返回值是另外一个函数，这样的函数称为高阶函数

"""

#对任意两个数字，整理之后再求和

#简单函数
def sum_num(a,b):
    return  abs(a) + abs(b)

#高级函数
def sum_num2(a,b,f):
    """

    :param a:
    :param b:
    :param f: 就是对两个数字进行整理
    :return:
    """
    return f(a) + f(b)
#通过绝对值整理之后再求和
print(sum_num2(2,-6,abs))
#通过平方之后再求和
print(sum_num2(2,-8,lambda n:n**2))




#第二种高阶函数
def t3(*args):
    def sum_nums():
        sum = 0
        for n in args:
            sum += n
        return sum
    return sum_nums
print(t3(2,4,6,8))  #区分:没加括号的话只是定义一个函数
print(t3(2,4,6,8)())    #加个括号菜表示调用函数