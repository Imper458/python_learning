# #读操作
# f = open('test.txt', 'r',encoding='utf-8')
# print(f.read())
# f.close()
#
# # #写操作
# # g = open('test.txt','w',encoding='utf-8')
# # for i in range(3):
# #     print(f'当前指针的位置是：',{g.tell()})
# #     g.write('hello' + '\n')
#
#
# # g.close()
#
# #指针的移动
# #需求：在第一个hello后面加一个world
#
# wf = open('test.txt','r+',encoding='utf-8')
# #把world第一和hello后面
# wf.seek(5,0)#从0开始，指针往后移动5个字符
# #把第一和hello后面的内容读取出来
# after = wf.read()#读完以后，指针又到了最后
#
# wf.seek(5,0)
# wf.write('world'+after)
# wf.close()



#with 语句来操作文件流
with open('test3.txt','w+',encoding='utf-8') as f:
    for i in range(10):
        f.write('hello\n')