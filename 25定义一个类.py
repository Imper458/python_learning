#描述一台汽车
class Car:

    def __init__(self,brand,name,category):
        print('开始初始化对象')
        #brand,name,category都是对象属性(成员属性)
        #品牌
        self.brand = brand
        #型号
        self.type_name = name
        #类型
        self.category = category

    def run(self):#成员函数
        print(f'{self.brand},{self.type_name},{self.category}')
        print('开起来')

    def __new__(cls,*args,**kwargs):
        print('创建Car的对象')
        return super().__new__(cls)

    def __str__(self):
        "str魔法函数：以后只要有print(对象)，则会自动调用__str__，并且打印str函数的返回值"
        return f'汽车的品牌是{self.brand}, 型号是：{self.type_name}, 汽车的类别是：{self.category}'

    def __del__(self):
        print('开始删除对象')


c1 = Car('byd','汉','jiaoche')
print(c1)
# c2 = Car('一汽大众','迈腾','中型轿车')
# c1.run()#调用对象的属性
# c2.run()
# print(c1.brand)#访问对象c1的属性

