# 包
# from socket import *
# import socket


# import socket
from socket import *


# 定义方法
# c++ 函数写法
# 修饰词 + 函数返回值 + 函数名 + (形参列表){
#
# }

# 标识方法的关键字def
def main():
    print("hello world")


def service_for_client(client):
    # 1. 接收客户端的请求
    request = client.recv(1024)
    print(request)

    # 2. 返回response
    # response包含响应头 + 响应体
    # 构造response
    response = "HTTP/1.1 200 OK\r\n"
    # response = response + "" 相当于下面的写法
    response += "Server: BWS/1.1\r\n"
    response += "\r\n"

    # 3. 拼接响应体
    response += "这是一个微型服务器!~牛逼???"

    # 4. 发送给客户端
    client.send(response.encode('gbk'))

    # 5. 下线关闭
    client.close()


# 1. 当前文件设置主函数入口
if __name__ == '__main__':
    # person p = new person()

    # 使用import socket
    # socket.socket()

    # 使用from socket import *
    # 1. 创建socket对象
    tcp_socket = socket(AF_INET, SOCK_STREAM)

    # 2. 绑定主机信息(地址+端口号)
    # 元组类型的参数 用()表示
    tcp_socket.bind(('', 7890))

    # 3. 监听
    tcp_socket.listen(128)

    # 4. 等着客户端来
    while True:
        # 4.1 等待客户链接服务器
        new_socket, client_info = tcp_socket.accept()
        print("--------客户端信息---------")
        print(client_info)

        # 请求头
        # GET / HTTP/1.1
        # nHost: 127.0.0.1:7890
        # Connection: keep-alive
        # Cache-Control: max-age=0
        # Upgrade-Insecure-Requests: 1

        # 4.2 调用服务客户的方法
        service_for_client(new_socket)

    # # 执行主函数(方法)
    # main()



