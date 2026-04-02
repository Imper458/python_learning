# 1.形参
def t1(x,y): #x和y也叫位置参数，也叫必要参数
    return x+y

result = t1(1,2)
print(result)

# 2.默认值参数
def t2(x,y,init_sum = 10):
     init_sum += x + y
     return init_sum

result2 = t2(1,2)
print(result2)


# 3.不定长传参
def t3(*args,init_sum = 10):
    print(type(args))
    if args:
        return init_sum + sum(args)

print(t3(1,2,100))


#4.不定长键值对
def t4(init_sum = 10,**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f'参数的名字{k},参数的值:{v}')
    return init_sum + sum(kwargs.values())


print(t4(x=10, y=20, z=30))



#位置参数-->默认传参-->不定长普通传参-->不定长键值对传参
def t5(a,b,c=100,*args,**kwargs):
    print(f'a是{a}')
    print(f'b是{b}')
    print(f'c是{c}')
    if args:
        h = c + sum(args)
        return h  #return了就会退出，后面的不会执行
    for k,v in kwargs.items():
        print(f'参数的名字{k},参数的值:{v}')
    return c + sum(kwargs.values())


print(t5(1, 2, 10, 11, 12, i=5))