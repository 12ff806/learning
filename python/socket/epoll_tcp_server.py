#!/usr/bin/env python3


import socket, select


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'


# 创建socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0)
serversocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# 创建epoll 将socket注册为epoll事件
epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    connections = {}
    requests = {}
    responses = {}

    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            # 服务器接受客户端连接
            if fileno == serversocket.fileno():
                connection, address = serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)

            # 接收客户端发送过来的数据
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)

            # 给客户端发送数据
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0)

            # 连接挂起状态 关闭连接
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]

finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

