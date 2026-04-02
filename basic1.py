str=('123456789')
print(str)#输出全部
print(str[0:-2])#输出第一个到倒数第二个
print(str[0])#输出第一个
print(str[2:5])#输出第3个到第6个，右侧不包含，左开右闭，最终就是第3个到第5个
print(str[2:])#输出第三个开始后的
print(str[1:5:2])#输出第2个到第5个，步长为2
print(str * 2)#输出字符串两次
print(str + '你好')#连接字符串
print('-'*50)
# !/usr/bin/python3

#input("\n按下 enter 键后退出。")
print(r'你好\n')#用\转义
x = 'runoob'; print(x)

#只用import没有导入函数
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#导入函数
from sys import path,argv
print('================Python import mode==========================')
print ('命令行参数为:')
for i in argv:   #因为已经导入函数，所以不需要用sys.argv
    print (i)
print('\n python 路径为', path)   #因为已经导入函数，所以不需要用sys.path

a='hello'
print(isinstance(a, list))
print(isinstance(0, bool))
print(isinstance(True, bool))
print(isinstance(False, bool))

tuple=('12347',2,'你好','我是你')
tuple2=('haha','qq')#元组最少要有两个元素
print(tuple)
print(tuple[0])#输出元组第一个元素
print(tuple[1:3])#输出元组第2个元素到第3个元素
print(tuple[2:])#输出元组第3以后的
print(tuple*2)
print(tuple + tuple2)

#集合
site = {'Google','Facebook','Yahoo','Twitter'}#创建site集合
print(site)

if 'Google' in site:
    print('Google在集合中')
else:
    print('Google不在集合中')

a = set('123456789')#集合不按顺序
b = set('a65993582')#集合里面有重复项的话会自动去掉
print(a)
print(b)
print(a|b)#并集
print(a - b)#差集
print(a & b)#交集


#字典
di = {}
di['one'] = "1 - 菜鸟教程"
di[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(di['one'])
print(di[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

dd = dict([('no1', 1), ('no2', 2)])
print(dd)


a,b,c = 1,2,3
print(a,b,c)