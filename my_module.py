__all__=['my_sum']#声明当前模型，只能公开my_sum函数    只针对from * import *
def my_sum(n):
    '''
    计算从0到n的和
    :param n: 正整数
    :return:
    '''
    s = 0
    for i in range(n):
        s += i
    return s

if __name__ == '__main__':
    print(my_sum(2))
    print(my_sum(3))

