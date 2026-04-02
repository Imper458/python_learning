
def sum_of_list(lst:list):
    sum = 0
    for number in lst:
        if isinstance(number,int) or isinstance(number,float):
            sum += number
    return sum




list = [1,2,3,4,5,'a',6]
print(sum_of_list(list))