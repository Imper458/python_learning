
def double_in_range(left,right):
    result = []
    for i in range(left,right+1):
        if i % 2 == 0:
            result.append(i)
    return result

begin = 4
end = 9
print(f'区间的偶数有：{double_in_range(begin, end)}')

data = [item for item in range(begin,end+1) if item % 2 == 0]
print(data)