'''
获取文件后缀名:os.path.splitext('/path/to/file.txt')
输出:('/path/to/file','.txt')

移动文件：
import shutil
shutil.move("aaa.jpg.txt","dir/bbb.txt.foo")
'''

import os
import shutil

origin_dir = os.path.join(os.path.dirname(__file__), 'arrange_dir')

print(origin_dir)

last_total_dir = []
for file in os.listdir(origin_dir):
    complete_file = os.path.join(origin_dir, file)
    the_file = file

    if os.path.isdir(complete_file):
        continue
    name_of_file = os.path.splitext(the_file)[0]
    last_name_of_file = os.path.splitext(the_file)[1]
    if last_name_of_file not in last_total_dir:
        last_total_dir.append(last_name_of_file)
    os.makedirs(os.path.join(origin_dir, last_name_of_file), exist_ok=True)

    target_dir = (os.path.join(origin_dir, last_name_of_file))
    target_file = os.path.join(target_dir, file)
    shutil.move(complete_file, target_file)

print('移动完成')


