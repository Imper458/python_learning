'''
1.目录不能有中文
2.excel，csv文件如果保存到了中文路径，要先用open函数给他打开，并赋值给一个名字例如f，再用pandas库中的pd.read_csv导入文件
3.查看函数形参快捷键 ： Ctrl + P
4.seaborn库版本过低，不能用histplot，要用distplot
5.注释快捷键：Ctrl + /
6.复制快捷键：CTRL + D
7.快速往下换行： Shift + Enter
8.代码往下移动：Ctrl + Shift + 向下方向键
9.优化代码格式：Ctrl + Alt + L
10.查看代码用法：Ctrl + Shift + i
11.快速往上换行：Ctrl + Alt + Enter
12.删除一行： Ctrl + Y
13.查找代码：Shift+Shift
14.取消缩进: Shift + Tab
15.更新seaborn，pandas,matplotlib包：以管理员身份运行anaconda prompt，
16.运行：ctrl+Shift+ F10
17.读取csv文件的时候，要加 encoding='gbk'
在窗口输入：
pip install --upgrade matplotlib
pip install pandas --upgrade
pip install seaborn --upgrade
pip install --upgrade numpy
'''

# 第一章 格式化输出
# 格式化输出
my_name = '威威'
my_age = 31
my_city = '北京'
print('我的名字是%s' % my_name)
print('我的名字是%s,我的年龄是%d,我的城市是%s' % (my_name, my_age, my_city))

# 第二种格式化输出
# f加{}
print(f'我的名字是{my_name},我的年龄是{my_age},我的城市是{my_city}')

# 特殊类型
money = 1111122
num = 1.765
print('我的金额是:%5d' % money)
print('我的身高是:%.1f' % num)  # 保留小数点后1位是.1f
print('我的身高是:%.2f' % num)  # 保留小数点后2位是.2f

# 精确的四舍五入
from decimal import Decimal

print(Decimal(str(num)).quantize(Decimal('0.00'), rounding='ROUND_HALF_UP'))

# 第二章 数学运算符
'''
2**4表示2的4次方
%表示取余数，也叫模运算
//表示整除，9//2==4
pow(a，b)表示幂函数运算,a 是底数，b是幂次
 注意：先计算后赋值(先计算复合表达式中的表达式，然后再复合计算){
  c+=a表示c=c+a
  c-=a表示c=c-a
  c*=a表示c=c*a
  c/=a表示c=c/a
  c**=a表示c=c**a
  在 x += 2 * 4 中，先计算2 * 4==8，然后再计算 x += 8；
  
  }
 
'''

print(9 % 2)
print(2 ** 3 ** 2)
print(2 ** 9)
print(pow(2, 2))

x = 11
x += 2 * 4
print(x)

