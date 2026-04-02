'''
简单列表，没有复合元素
'''
def sort_list(lst:list):
    result = lst
    # lst.sort()
    # return sorted(result)
    return sorted(result,reverse=True)

lst = [1,2,3,9,99,6]
print(sort_list(lst))