import socket
from datetime import datetime

HOST = 'localhost'
PORT = 10009


def echo_server():
    ''' Echo Server's Server '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机端口上
    s.bind((HOST, PORT))
    # 只接受一个连接
    s.listen(1)
    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connect by {addr}')
        # 将收到的数据以及时间写入文件中并返回
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            with open('./week02/HomeWork/files_to_send/send_to_client.txt',
                      'ab') as f:
                f.write(f'\nyou added the info: {data}, this file is sended at: {datetime.now()}'.encode())
            with open('./week02/HomeWork/files_to_send/send_to_client.txt',
                      'rb') as f:
                conn.sendall(f.read())
        conn.close()
    s.close()


if __name__ == "__main__":
    echo_server()
