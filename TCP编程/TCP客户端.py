import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.6.1',8000)
client_socket.connect(('192.168.6.1',8000))

while True:
    send_msg = input('客户端>>')
    if send_msg == 'quit':
        client_socket.send(send_msg.encode('utf-8'))
        break

    client_socket.send(send_msg.encode('utf-8'))

    msg = client_socket.recv(1024).decode('utf-8')

    print(f'来自服务端IP:{server_address[0]},端口号：{server_address[1]}:{msg}')

client_socket.close()
