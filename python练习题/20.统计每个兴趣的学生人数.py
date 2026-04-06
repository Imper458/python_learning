import os

file_path = os.path.join(os.path.dirname(__file__),r'datas\many_texts\student_like.txt')
print(file_path)
with open(file_path,'r',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    #['小张 篮球,羽毛球\n', '小王 篮球,乒乓球\n', '小李 篮球,台球\n', '小赵 篮球,台球，足球\n', '小孙 羽毛球,台球\n', '小钱 台球\n', '小强 乒乓球']
    hobby = {}
    for line in lines:
        line = line.split(' ')
        # print(line[1].strip('\n'))
        for like in line[1].strip('\n').split(","):
            if like not in hobby:
                hobby[like] = 1
            else:
                hobby[like] += 1

print(hobby)