'''
方法1：按行合并
for line in file:

方法2：一次读取所有内容到一个字符串
content = f.read()
'''
import os


many_texts_file = os.path.join(os.path.dirname(__file__),r'datas\many_texts')
print(f'many_texts_file:{many_texts_file}')
def merge_txt_file():
    contents = []
    for file in os.listdir(many_texts_file):
        each_file = os.path.join(many_texts_file, file)
        if os.path.isfile(each_file) and file.endswith('.txt'):
            with open(each_file,'r',encoding='utf-8') as f:
                contents.append(f.read())
    final_content = '\n'.join(contents)
    print(final_content)

    return final_content

def write_txt_file(contents):
    with open(os.path.join(os.path.dirname(__file__),r'datas\write.txt'),'w',encoding='utf-8') as f:
        f.write(contents)
    pass
print(merge_txt_file())
write_txt_file(merge_txt_file())

