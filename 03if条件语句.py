"""
年龄判断：由用户输入
如果是0~18岁：未成年
如果是18~60岁：打工仔
如果是60~100岁：老年人

"""
age = int(input('请输入你的年龄:'))

# if age >=0 and age <18:
if 0 <= age < 18:
    print(f'你的年龄是:{age},你是未成年')
elif 18 <= age < 60 :
    print(f'你的年龄是:{age},你是打工仔')
else:
    print(f'你的年龄是:{age},你是老年人')


#三目条件运算符
#返回条件一的值1 if 条件 else 返回不满足条件的值2
num = int(input('请输入一个整数：'))
result = f'当前的数字{num}是偶数' if num % 2 ==0 else f'当前的数字{num}是奇数'
print(result)

