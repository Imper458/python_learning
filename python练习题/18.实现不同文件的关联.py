import os
def read_file(path):
    with open(path,'r',encoding='utf-8') as f:
        data = []
        for line in f.readlines():
            line = line[:-1]
            data.append(line.split('，'))
        # print(data)
        #[['语文', '101', '小张', '94'], ['数学', '101', '小张', '88'], ['英语', '101', '小张', '92'], ['语文', '102', '小王', '76'], ['数学', '102', '小王', '95'], ['英语', '102', '小王', '82'], ['语文', '103', '小李', '89'], ['数学', '103', '小李', '78'], ['英语', '103', '小李', '96'], ['语文', '104', '小赵', '65'], ['数学', '104', '小赵', '85'], ['英语', '104', '小赵', '72'], ['语文', '105', '小强', '91'], ['数学', '105', '小强', '98'], ['英语', '105', '小强', '89']]

        return data

    pass

def merge_file_data(data1,data2):

    for row in data1:
        for row2 in data2:
            if row[0] == row2[0]:
                row.append(row2[1])
    return data1



    pass



path_student = 'course_student_grade_input.txt'
path_teacher = 'course_teacher.txt'

full_path_student = os.path.join(os.path.dirname(__file__),path_student)
full_path_teacher = os.path.join(os.path.dirname(__file__),path_teacher)
# print(full_path_student)
# print(full_path_teacher)
student = read_file(path_student)
teacher = read_file(path_teacher)
# print(student)
# print(teacher)
#[['语文', '101', '小张', '94'], ['数学', '101', '小张', '88'], ['英语', '101', '小张', '92'], ['语文', '102', '小王', '76'], ['数学', '102', '小王', '95'], ['英语', '102', '小王', '82'], ['语文', '103', '小李', '89'], ['数学', '103', '小李', '78'], ['英语', '103', '小李', '96'], ['语文', '104', '小赵', '65'], ['数学', '104', '小赵', '85'], ['英语', '104', '小赵', '72'], ['语文', '105', '小强', '91'], ['数学', '105', '小强', '98'], ['英语', '105', '小强', '89']]
#[['语文', '于老师'], ['数学', '张老师'], ['英语', '王老']]
print(merge_file_data(student, teacher))
#[['语文', '101', '小张', '94', '于老师'], ['数学', '101', '小张', '88', '张老师'], ['英语', '101', '小张', '92', '王老'], ['语文', '102', '小王', '76', '于老师'], ['数学', '102', '小王', '95', '张老师'], ['英语', '102', '小王', '82', '王老'], ['语文', '103', '小李', '89', '于老师'], ['数学', '103', '小李', '78', '张老师'], ['英语', '103', '小李', '96', '王老'], ['语文', '104', '小赵', '65', '于老师'], ['数学', '104', '小赵', '85', '张老师'], ['英语', '104', '小赵', '72', '王老'], ['语文', '105', '小强', '91', '于老师'], ['数学', '105', '小强', '98', '张老师'], ['英语', '105', '小强', '89', '王老']]




#方法二：把老师txt用字典存起来
def dict_file(path):
    with open(path,'r',encoding='utf-8') as f:
        result = {}
        for line in f.readlines():
            line = line[:-1]
            subject ,teacher = line.split('，')
            result[subject] = teacher
            # print(result)
        return result
    {'语文': '于老师', '数学': '张老师', '英语': '王老'}

def merge_dict_file(path,dt:dict):
    with open(path,'r',encoding='utf-8') as f:
        data = []
        for line in f.readlines():
            line = line[:-1]
            subject,sno,name,grade = line.split('，')
            teacher = dt.get(subject)
            data.append([subject,sno,name,grade,teacher])
        # print(data)
        #[['语文', '101', '小张', '94', '于老师'], ['数学', '101', '小张', '88', '张老师'], ['英语', '101', '小张', '92', '王老师'], ['语文', '102', '小王', '76', '于老师'], ['数学', '102', '小王', '95', '张老师'], ['英语', '102', '小王', '82', '王老师'], ['语文', '103', '小李', '89', '于老师'], ['数学', '103', '小李', '78', '张老师'], ['英语', '103', '小李', '96', '王老师'], ['语文', '104', '小赵', '65', '于老师'], ['数学', '104', '小赵', '85', '张老师'], ['英语', '104', '小赵', '72', '王老师'], ['语文', '105', '小强', '91', '于老师'], ['数学', '105', '小强', '98', '张老师'], ['英语', '105', '小强', '89', '王老师']]

        return data



dict_result = dict_file(full_path_teacher)
print(merge_dict_file(full_path_student, dict_result))