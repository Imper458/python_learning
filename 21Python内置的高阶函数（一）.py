"""
一：map函数
map函数接收的事两个参数，一个是函数名，
另外一个是序列，其功能是将序列中的数值作为函数的参数依次传入到函数中执行，然后再返回列表中。返回值是一个迭代器对象
"""

print(list(map(lambda n: n ** 2, [1, 2, 3, 4, 5, 6])))


"""
reduce函数
reduce函数也是一个参数为函数，另一个参数为序列的对象（比如：list列表）。(必须要有两个参数)
其返回值为一个值而不是迭代器对象，故其常用于叠加，叠乘等等
"""

from functools import *

print(reduce(lambda x, y: x + y, [2, 4, 6, 8, 10],40))


#案例：给你一个很长的字符串，统计每个单词出现的次数

str1 = 'hello world python hello java hello python java python geajn'
#第一步：把单词切开
lst = str1.split(' ')
print(lst)
#第二步:每个单词只要出现了就代表有一次
new_lst = list(map(lambda item: {item: 1}, lst))
print(new_lst)
#第三步：调用reduce实现相同单词的叠加
def func(dict1,dict2):
    #把dict1作为叠加的返回字典
    key = list(dict2.items())[0][0] #得到dict2中的key（单词：world）
    value = list(dict2.items())[0][1] #得到dict2中value（1）
    dict1[key] = dict1.get(key,0) + value   #get()函数是根据他的key得到他的value值,如果没有这个key就返回0
    return dict1


print(reduce(func, map(lambda item: {item: 1}, str1.split(' '))))