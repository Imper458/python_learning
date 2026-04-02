import os
file_path = 'course_student_grade_input.txt'

#读取文件
def read_file(file_path):
    full_file_path = os.path.join(os.getcwd(), file_path)
    with open(full_file_path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            line = line.strip()
            parts = line.split('，')
            row = {
                '科目': parts[0],
                '学号': parts[1],
                '姓名': parts[2],
                '分数': int(parts[3])
            }
            lines.append(row)
        # print(lines)
        return lines

def calculate_grade(data:list):
   subject_data = {}
   for person in data:
      subject = person['科目']
      #如果没有科目就先创建科目
      if subject not in subject_data:
          subject_data[subject] = []
      subject_data[subject].append(person)
   print(subject_data)

   result = []
   for subject,students in subject_data.items():
       max_student = max(students, key=lambda x:x['分数'])
       min_student = min(students, key=lambda x:x['分数'])

       all_score = [s['分数'] for s in students]
       avg_score = sum(all_score)/len(all_score)
       result.append(
           {
               "科目": subject,
               "最高分": max_student['分数'],
               "最高分得主":max_student['姓名'],
               "最低分": min_student['分数'],
               "最低分得主": min_student['姓名'],
               "平均分": avg_score,

           }
       )


   return result

data = read_file(file_path)
print(calculate_grade(data))