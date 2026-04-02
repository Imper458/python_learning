set1 = set()
set1 = {'abcdefg',100,78,3.14}
print(len(set1))
print(set1)

#添加
set1.add('hello')
set1.add(9999)
print(set1)

#删除
set1.remove('hello')
print(set1)

# for可以遍历
set2 = {2,'hello',(100,200)}  #set里不能放可变类型，比如列表
print(set2)