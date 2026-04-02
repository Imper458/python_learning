#计算一个正整数的阶乘
def t1(n:int)-> int:
    """
    计算函数的阶乘
    :param a:
    :return:
    """
    if n == 1:
        return 1     #递归函数的出口
    return n * t1(n-1)


print(t1(6))