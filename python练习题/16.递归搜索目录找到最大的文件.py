import os
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
#D:\PythonProject\pythonProject\python_learning\python练习题

def get_max_file(dir_path):
    max_file =  {'文件名':'','文件大小':0}
    for file in os.listdir(dir_path):
        full_file_path = os.path.join(dir_path, file)
        if os.path.isfile(full_file_path):
            file_size = os.path.getsize(full_file_path)
            if file_size > max_file['文件大小']:
                max_file['文件名'] = file
                max_file['文件大小'] = file_size
            # else:
            #     continue  #if执行完会自动进入下一轮，不用continue
        elif os.path.isdir(full_file_path):
            sub_max = get_max_file(full_file_path)  #注意要用sub_max接住get_max_file的return值，return的是一个字典
            if sub_max['文件大小'] > max_file['文件大小']:
                max_file= sub_max
    return(max_file)


print(get_max_file(dir_path))