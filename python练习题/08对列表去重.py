'''
输入：重复列表[10,11,12,11,12]
返回：[10,11,12]
'''
def list_out_of_double(lst:list) -> list:
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result



a = list_out_of_double([10,11,12,11,12])
print(a)

#把列表变成集合，在把集合变成列表

lst = [10,11,12,11,12]


print(list(set(dict.fromkeys(lst, None))))
print(dict.fromkeys(lst, None))