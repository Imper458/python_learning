'''
原始列表:[3,5,7,9,11,13]
移除元素:[7,11]

返回：[3,5,9,13]
'''

def out_of_list(lst1:list,lst2:list) -> list:
    l1 = lst1
    l2 = lst2
    for item in l2:
        if item not in l1:
            print(f"这个元素'{item}'不在原始列表中")
            return [item for item in l1]
        else:
            l1.remove(item)
    return l1

last = out_of_list([1,2,3,4,5,6],[4,5,6,7])
print(last)