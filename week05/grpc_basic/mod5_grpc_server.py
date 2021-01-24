# grpcio 是启动 gRPC 服务的项目依赖
# pip install grpcio
# gRPC tools 包含 protocol buffer 编译器和用于从 .proto 文件生成服务端和客户端代码的插件。
# pip3 install grpcio-tools
# 升级protobuf
# pip install --upgrade protobuf


import grpc
import time
import schema_pb2
import schema_pb2_grpc
# 实现多线程
from concurrent import futures


# 编写类完成proto定义的服务。继承service定义的GatewayServicer。函数同定义的call方法。
# 注意4点：1、继承gateway
class GatewayServer(schema_pb2_grpc.GatewayServicer):

    # 2、定义函数
    def Call(self, request_iterator, context):
        # 3、接收请求
        for req in request_iterator:
            # 4、接收请求参数
            # 获取请求中的值，进行处理。利用response方法返回。
            yield schema_pb2.Response(num=req.num+1)
            time.sleep(1)


def main():
    # 使用线程池的方法。
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 将上述服务类添加到server里面。
    schema_pb2_grpc.add_GatewayServicer_to_server(GatewayServer(), server)
    # 定义端口
    server.add_insecure_port('[::]:50051')
    # 开始执行
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()


