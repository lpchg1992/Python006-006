import grpc
import queue
import schema_pb2_grpc
import schema_pb2

queue = queue.Queue()

def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        # 注意客户端的方法。
        stub = schema_pb2_grpc.GatewayStub(channel)
        queue.put(1)
        # 调用功能，取用推入queue中的数据。
        resp = stub.Call(generate_message())
        for r in resp:
            num = r.num
            queue.put(num)

def generate_message():
    while True:
        num = queue.get()
        print(num)
        # 从队列中取出1，然后依照定义的数据结构，发送请求数据，此处为num
        yield schema_pb2.Request(num=num)

if __name__ == "__main__":
    main()