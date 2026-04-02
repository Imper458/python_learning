# 1.修改列表
lst = [12,'ab',3.14,[1,2],12]
lst[1] = 'abc'
print(lst)

# 列表中不能用find（），要用index（）
print(lst.index(12))
print(lst.count(12))
print(len(lst))

#append()
lst.append('hello') #append（），在列表最后添加字符串
print(lst)

#extend()
lst.extend('world') #extend(),也是在列表最后添加字符串，不过是把字符串拆开一个个添加
print(lst)

#插入
lst.insert(1,'嘻嘻')  #insert(),在列表指定标签位置插入新的字符串
print(lst)

#删除操作
#pop()根据下标删
lst.pop(3)
print(lst)

#del()根据下标删
del lst[1]
print(lst)

#remove()根据值删,只删除第一个
lst.remove(12)
print(lst)

#逆序
#[::-1]
print(lst[::-1])
#reserve()
lst.reverse()
print(lst)

lst2 = [4,9,98,32,2,12]
lst2.sort()
print(lst2)

for i in lst:
    print(i)