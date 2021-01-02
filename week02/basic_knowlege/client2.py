import socket
# 使用socket类。AF_INET表示IPV4地址，socket.SOCK_STREAM表示TCP连接。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 得到s对象

# debug
print(f"s1 : {s}")
# fd=6 6是指文件描述符。之前说过：0是标准输入，1是标准输出，2是错误输出。
# s1 : <socket.socket fd=6, family=AddressFamily.AF_INET, type=SocketKind \
# .SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>

s.connect(('www.httpbin.org', 80))

# debug
print(f"s2 : {s}")
# 获取到了本地ip以及端口，
# s2 : <socket.socket fd=6, family=AddressFamily.AF_INET, type=SocketKind \
# .SOCK_STREAM, \
# proto=0, laddr=('192.168.2.103', 37032), raddr=('54.158.248.248', 80)>

# 在socket层面，需要发送HTTP协议的请求，在应用层由于自动封装，则不用。
s.send(b'GET / HTTP/1.1\r\nHOST:time.geekbang.org\r\nConnection: close\n\r\n')

buffer = []

# 接收
# 需要返回状态码，头部，内容
while True:
    # 每次接受指定大小的字符，接收的是httpbin.org的数据
    data = s.recv(1024)
    if data:
        buffer.append(data)
    else:
        break
# 服务端关闭连接
s.close()

# 由于接收的是二进制数据，因此也要用b''连接
response = b''.join(buffer)

# 指定最大分割次数
header, html = response.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

# wb写入二进制文件
with open('index.html', 'wb') as f:
    f.write(html)
