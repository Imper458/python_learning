# 1.数学运算符(拼接，重复，比较)
s1 = 'abc' + 'efg'
print(s1)

# 列表相加
lst = [100]
lst2 = lst + [1,3.14]
print(lst2)
# 列表相乘(表示重复的意思)
print('-'*50)
print([1,2]*2)
lst *= 10
print(lst)

lst3 = ['abc',1,2]
lst4 = ['abc',3,1]
print(lst3 < lst4)


# 2.内置函数
t1 = (100,200)
print(max(t1))
print(min(t1))
print(sum(t1))

print(max('hellow'))