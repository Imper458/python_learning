s1 = 'I\'m Tom'
print(s1)
s2 = "我是\"湖南\"人"
print(s2)
#切片包头不包尾 s[0,3]是从标签为0开始到标签为2结束
s3='abcdefghijk'
print(s3[::-1]) #把字符串倒序输出

#字符串的函数
#find函数和index函数，有的话就返回首个字符串的下标，没有就返回-1,可以用来做判断

ss = 'hellopythonworld'
print(ss.find('ph'))
print(ss.index('py'))

"""
大小写转化
upper()全都变成大写
lower()全都变成小写

分割字符串
split(seq = "",num = string.count(str))
partition(str)  找到字符串中的第一个str，并以str为界，将字符串分割成三部分，返回一个新的元组
"""


#字符串切割
sss = 'I am a student'
print(sss.split(' '))   #分割出来一个列表,分隔符不会在列表中出现
print(sss.partition('a'))   #分区域,分隔符单独一个区

#替换
print(sss.replace('student', 'worker'))

#strip去掉两端多余字符串