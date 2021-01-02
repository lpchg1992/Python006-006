import socket

HOST = 'localhost'
PORT = 10000


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
        # 这种写法可以避免停止接收请求
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # 此时unicode需要被解码
            data = data.decode('utf-8')
            print(f'received : {data}')
            # 编码成unicode
            data = data.encode()
            conn.sendall(data)
        conn.close()
    s.close()


if __name__ == "__main__":
    echo_server()
