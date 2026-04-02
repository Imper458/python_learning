'''
输入文件：
三列：学号，姓名，成绩
列之间用逗号分割，比如”101，小张，88
'''
from pathlib import Path

file_path = Path(__file__)

def read_file():
    lines = []
    with open('./student_grade_input.txt','r',encoding='utf-8') as f:
        for line in f.readlines():

            line = line[:-1]#去掉每行末尾的换行符
            # clean_data = line.strip()
            # lines.append(clean_data.split(','))
            lines.append(line.split(','))
        return lines

def sort_grade(data:list):
    datas:list = sorted(data,key=lambda x:int(x[0]))
    return datas


def write_file(datas:list):
    with open('./student_grade_output.txt','w',encoding='utf-8') as f:
        for data in datas:
            f.write(','.join(data)+'\n')
#读取文件..

data = read_file()
print(data)
#排序数据
datas = sort_grade(data)
print(datas)
# #写出文件

write_file(datas)
print(datas)