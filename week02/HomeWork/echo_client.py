import socket
from datetime import datetime

HOST = 'localhost'
PORT = 10009


# 当程序内容增多，可以整理并抽象代码到函数
def echo_client():
    '''
    Echo Server's Client
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 接收用户数据并发送服务端
        data = input('input some words you want to add to the file > ')

        # 设定退出条件
        if data == 'exit':
            break

        # 发送数据到服务端
        # encode不写参数即编码为二进制
        s.sendall(data.encode())

        # 接收服务端数据
        # 将时间作为收到文件的文件名
        data = s.recv(1024)
        if not data:
            break
        else:
            with open(f'./week02/HomeWork/received_files/{datetime.now()}.txt',
                      'ab') as f:
                f.write(data)

    s.close()


if __name__ == "__main__":
    echo_client()
