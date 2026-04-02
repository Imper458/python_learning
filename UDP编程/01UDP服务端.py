import socket
#实现，客户端与服务端的即时聊天

#创建一个UDP的socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#IP:127.0.0.1,其他主机不可以和当前的服务器端通信，除非客户端也在本地
#192.168.6.1 ,其他主机可以和当前的服务器端通信
#IP:'',该服务端绑定到所有的IP上
server_socket.bind(('192.168.6.1', 6666))

##注意，recvfrom是一个阻塞的函数，如果没有收到数据包，那么程序暂停到这不动




while True:
    print('开始阻塞')
    #msg是收到的数据，addr是源地址和端口号
    msg, addr = server_socket.recvfrom(1024*10)#最多接受10kb的数据包
    if msg.decode('utf-8') == 'quit':
        break
    #decode可以把 字节数据 转换成字符串
    print(f'来自IP:{addr[0]},端口号：{addr[1]}的消息：{msg.decode("utf-8")}')

    #服务端也可以发送数据到客户端
    send_msg = input('服务端>>')
    #seedto发送的数据不能是字符串，只能是字节数据，字符串的encode函数
    server_socket.sendto(send_msg.encode('utf-8'),addr)

#最后要关闭socket
server_socket.close()

