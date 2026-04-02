# 计算0~100的所有奇数的和
# {方法一 range（）函数里没用步长
my_sum1 = 0
n1 = 1
for n1 in range(1, 100):  # range()函数是左闭右开，也就是[1,100)
    if n1 % 2 == 1:
        my_sum1 += n1
    n1 += 1
print(f'my_sum1结果是{my_sum1}')

# 方法二 range（）里加上步长
my_sum2 = 0
n2 = 1
for n2 in range(1, 100, 2):
    my_sum2 += n2
print(f'my_sum2结果是{my_sum2}')

# 方法三 range里只写一个值，默认从0开始，步长为1
my_sum3 = 0
n3 = 1
for n3 in range(100):
    if n3 % 2 == 1:
        my_sum3 += n3
print(f'my_sum3结果是{my_sum3}')

# 方法四 用break
n4 = 0
my_sum4 = 0
while True:
    n4 += 1
    if n4 > 100:
        break
    if n4 % 2 != 0:
        my_sum4 += n4
print(f'my_sum4结果是{my_sum4}')

# 方法五 用continue
n5 = 0
my_sum5 = 0
for n5 in range(1, 100):
    if n5 % 2 == 0:
        continue
    my_sum5 += n5
print(f'my_sum5结果是{my_sum5}')

# 输出九九乘法表
for i in range(1, 10):  # 代表行数
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    print()

# 输出九九乘法表
i = 1
while i <= 9:  # 代表行数
    j = 1
    while True:  # 把该行的所有算式都输出来
        if j > i:
            break
        print(f'{i}*{j}={i * j}', end='\t')
        j += 1
    i += 1
    print()
