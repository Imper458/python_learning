def my_abs(num):
    """
    该函数是为了可以返回注释的绝对值。
    :param num:传入的数字，必须是个数字，而且必传
    :return:返回该数字的绝对值
    """
    if num < 0:
        return (-num)
    else:
        return (num)
print(my_abs(-9))


# 在python3.5之后，可以对函数参数和返回值进行类型的声明
def new_abs(num: int) -> int:
    """
该函数是为了可以返回注释的绝对值。
:param num:传入的数字，必须是个数字，而且必传
:return:返回该数字的绝对值
    """
    if num < 0:
        return -num
    else:
        return num

print(new_abs(-9))

