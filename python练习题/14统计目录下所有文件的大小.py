import os

project_path =  os.getcwd()

print(f'当前工作目录是{project_path}')

total_size = 0
for dirpath, dirname, filenames in os.walk(project_path):
    print(f'dirpath是:{dirpath}')
    print(f'dirname:{dirname}')
    print(f'filename:{filenames}')

    for filename in filenames:
        print(filename)
        print(os.path.join(dirpath, filename))
        total_size += os.path.getsize(os.path.join(dirpath, filename))

print(total_size)


###用递归函数实现

def get_file_size(path):
    names_list = os.listdir(path)
    # print(names_list)
    total_size = 0

    for name in names_list:
        file_abspath = os.path.join(path, name)
        # print(file_abspath)
        if os.path.isfile(file_abspath):
           total_size += os.path.getsize(file_abspath)

        elif os.path.isdir(file_abspath):
            total_size += get_file_size(file_abspath)
    return(total_size )




parent_path = os.path.dirname(project_path)
print(parent_path)
print(get_file_size(parent_path))