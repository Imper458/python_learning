#计算0~100的所有奇数的和
my_sum = 0
n = 1
while 0 <= n <= 100:
    if n % 2 == 1:
        my_sum += n
    n += 1
print(f'结果是{my_sum}')


#输出九九乘法表
i = 1
while i <= 9:   #代表行数
    j = 1
    while j <= i :  #把该行的所有算式都输出来
        print(f'{i}*{j}={i*j}',end='\t')
        j += 1
    i += 1
    print()




