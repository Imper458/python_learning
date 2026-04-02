import socket

#创建一个UDP的socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#客户端的socket是不需要bind的，所有由操作系统分配一个随机的端口号

while True:
    #发送消息给服务端
    send_msg = input('客户端>>')
    if send_msg == 'quit':
        #把quit发给服务器，然后客户端退出循环
        client_socket.sendto(send_msg.encode('utf-8'), ('192.168.6.1', 6666))
        break
    #sendto必须要指定目标地址和目标端口号
    client_socket.sendto(send_msg.encode('utf-8'),('192.168.6.1',6666))

    #接受服务器，发过来的数据
    msg,addr = client_socket.recvfrom(1024)
    # decode可以把 字节数据 转换成字符串
    print(f'来自IP:{addr[0]},端口号：{addr[1]}的消息：{msg.decode("utf-8")}')

client_socket.close()