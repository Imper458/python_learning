
def read_file():
    with open('./student_grade_input.txt',encoding='utf-8') as f:
        last_col = []
        scores = []
        for line in f.readlines():
            # clean = line.strip()
            # lines.append(clean)
            line = line[:-1]
            field = line.split(',')
            scores.append(int(field[-1]))
    max_grade = max(scores)
    min_grade = min(scores)
    average = sum(scores)/len(scores)
    return max_grade,min_grade,average
    pass


#读取文件
data = read_file()
print(data)
#统计
