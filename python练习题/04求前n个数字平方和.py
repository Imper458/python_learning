def sum_of_squares(num):
    sum = 0
    for i in range(1,num+1):
        sum += i**2

    return sum

a = 5
print(sum_of_squares(a))