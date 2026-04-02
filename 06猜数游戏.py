print('-'*50)
print('欢迎来到猜数游戏')
print('规则一:系统每次自动生成一个1~10的随机数')
print('规则二:每次游戏只能猜3次')
print('规则三:进入游戏或者继续玩，输入：yes或者y')
print('规则四:离开游戏，输入：no或者n')
print('-'*50)

import random
n = 0
while True:
    order = input('请输入是否开始游戏:')
    if order == 'yes' or order == 'y':  #用户想玩游戏
        number = random.randint(1,9)   #生成一个随机数,[1,9] randint包头也包尾
        n += 1
        for i in range(1,4):    #用户最多可以猜三次
            print(f'这是你的第{n}次游戏')
            my_num = int(input('请玩家输入所猜的数字:'))
            if my_num == number:
                print(f'恭喜你，你猜中了，答案就是{my_num}')
                break
            elif my_num > number:
                print(f'很遗憾你没有猜中，你猜的数字太大了,还剩下{3-i}次机会')
                n += 1
            else:
                print(f'很遗憾你没有猜中，你猜的数字太小了,还剩下{3-i}次机会')
                n += 1
        else:    #三次都猜错了
            print(f'很遗憾三次你都猜错了，正确答案是{number}')
        break
    elif order == 'no' or order == 'n':
        print('谢谢,GAME OVER!!')
        break
    else:
        print('请输入正确的指令！')



