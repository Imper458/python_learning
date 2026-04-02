def t1():
    print('hello,执行函数test1')
    return   #没有返回值就返回None
    print('1')

result = t1()
print(result)

def t2(x,y):
    x2 = x**2
    y2 = y**2
    return x2,y2
result2 = t2(3,4)
print(result2)
print(type(result2))
r1,r2 = t2(5,6)
print(r1,r2)
