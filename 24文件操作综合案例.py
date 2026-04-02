import os

#给与一个目录：
#需求：把该目录中（该目录可能存在子目录）所以的.py文件拷贝到另一个指定的目录中

def copy_dir(source_dir, destination_dir):
   '''
   把source_dir中的.py文件拷贝到destination_dir中
   :param sourc_dire: 原始目录
   :param destination_dir: 目标目录
   :return: 返回一共拷贝多少个文件数
   '''
   count = 0
   for f in os.listdir(source_dir):#其中的f代表目录下的每个文件的名字
      # 把文件名和目录拼凑成一个完整的绝对路径
      f_path = os.path.join(source_dir, f)
      if os.path.isfile(f_path) and f.endswith('.py'):#表示f是一个普通文件，同时也是py文件
         #拷贝该文件
         if not os.path.exists(destination_dir):#，目标目录不存在
            os.makedirs(destination_dir)
         #拼凑一个拷贝之后的目标文件绝对路径
         sink_path = os.path.join(destination_dir, f)
         #拷贝文件内容到sink_path中
         num = copy_file(f_path, sink_path)
         count += num
      elif os.path.isdir(f_path):#表示f是一个目录
         # 采用递归函数的写法：
         # 为了保持同样的目录结构，目标目录要跟着变化
         new_destination_path = os.path.join(destination_dir,f)
         copy_dir(f_path, new_destination_path)
   return count




def copy_file(source_file, sink_file):
   '''
   拷贝文件内容，把原始文件的绝对路径拷贝到目标文件的绝对路径
   :param source_file: 原始文件的绝对路径
   :param sink_file: 目标文件的绝对路径
   :return: 拷贝成功之后返回1
   '''

   # #第一种：考虑到文件都是小文件：可以一次性读取全部文件内容，并且一次性写入文件
   # with open(source_file, 'r', encoding='utf-8') as source_f:
   #    content = source_f.read()
   #    with open(sink_file, 'w', encoding='utf-8') as sink_f:
   #       sink_f.write(content)

   #考虑到文件比较大，每次从源文件中读取一部分内容，并且写入到新文件中（循环多次）
   source_f = open(source_file, 'r', encoding='utf-8')
   sink_f = open(sink_file, 'w', encoding='utf-8')

   while True:
      content = source_file.read(1024*10)#每次读10kb
      if content =='' or content is None:
          break#意味着文件读完了
      sink_f.write(content)
      sink_file.close()
      source_file.close()

   return 1