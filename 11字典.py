# 创建字典
dict1 = {'name': 'Tom', 'age': 22}
dict2 = {}  # 空字典
dict3 = dict([('name', 'haha'), ('age', 11)])
dict4 = dict(name='haha', age=11, city='gz')

#新增和修改
dict1['address'] = 'shanghai '
dict1['age'] = 11
print(dict1)

#删除字典中的全部项:celar（）
dict3.clear()
print(dict3)
#删除个别项pop()
dict4.pop('age')
print(dict4)
#del
del dict4['city']
print(dict4)

#查询
if 'address' in dict1:
    print(dict1['address'])

new_dict = dict.fromkeys(['name','age'])
print(new_dict)
new_dict['name'] = '王五'
print(new_dict)

#字典的遍历

#items是把字典中所有的项放到一个列表中
for k,v in dict1.items():
    print(f'key = {k} , value ={v} ')

#keys()
for k in dict1.keys():
    print(k)

#values()
for v in dict1.values():
    print(v)




print('*'*60)
print('练习阶段')
#创建一个字典
a = dict([('name','呵呵'),('age',8)])
print(a)
zidian = {'mingzi':'wangxiaofan','sex':"female"}
print(zidian)
#新增：
a['address'] = 'guangzhou'
print(a)
#修改
a['name'] = 'ww'
print(a)

#删除部分
a.pop('address')
print(a)

#查询
if 'age' in a:
    a['age'] = 22
    print(a['age'])

for k,v in a.items():
    print(f'{k} = {v}')

for k in a.keys():
    print(f'key={k}')

for v in a.values():
    print(f'value={v}')