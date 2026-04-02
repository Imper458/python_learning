h = float(input('请输入你的身高(单位：米):\t'))
w = float(input('请输入你的体重(单位：kg):\t'))

BMI = w/(h ** 2)  #体重除以身高的平方  BMI = w/h ** 2   不加括号也可以
print(f'你的身高是:{h}米,',end = '')
print(f'你的体重是:{w}kg,',end = '')
print(f'你的BMI指数是:{BMI}')
