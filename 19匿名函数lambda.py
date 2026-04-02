"""
1.lambda表达式的参数可有可无
2.函数的参数在lambda表达式中完全适用
3.lambda表达式能接受任何数量的参数但只能返回一个表达式的值
4.直接打印lambda表达式，输出的是此lambda的内存地址

"""

# 使用匿名函数计算两个数字的和
fn = lambda x, y: x + y
print(fn(10, 20))

# 需要给某个复杂的列表排序
lst = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41}
]
# 根据年龄排序
lst.sort(key=lambda item: item['age'])
print(lst)

# 求和 用lambda来写：
s = lambda z=100, *args: z + sum(args)
print(s(5, 4))


# 用函数来写：
def total(*args: float) -> float:
    if args:
        s = 0
        h = s + sum(args)       #注意args要加sum（），因为args是元组，不能和数字相加
        return h


print(total(2.1,6,6))





print('*'*50)
lst1 = [
    {'name': '张三', 'age': 34},
    {'name': '李四', 'age': 16},
    {'name': '王五', 'age': 41}
]
lst1.sort(key=lambda item: item['age'])


def t(a,*args:float,**kwargs):
    if args:
        q = a + args[0]
        qw = sum(args)
        print(q,qw)
    for k,v in kwargs.items():
        print(f'keys:{k},values:{v}')

print(t(1,2,3,4,x=1,y=6,z=66))


u = lambda q,*args:q*2+sum(args)
print(u(6,3,6,3,0))