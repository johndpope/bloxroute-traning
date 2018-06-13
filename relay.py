import sys
import socket
import timeit
import select

FILE_CHUNK_SIZE = 80000

listen_port = int(sys.argv[1])
ip1, port1 = sys.argv[2], int(sys.argv[3])

ip2, port2 = sys.argv[4], int(sys.argv[5])
ip3, port3 = sys.argv[6], int(sys.argv[7])

print('Opening connection to receiver 1')
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((ip1, port1))

print('Opening connection to receiver 2')
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect((ip2, port2))

print('Opening connection to receiver 3')
socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket3.connect((ip3, port3))

print('Open socket listener')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', listen_port))
serversocket.listen(1)
serversocket.setblocking(0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)
print('Socket connection opened successfully')

try:
    connections = {}; requests = {}; responses = {}
    while True:
    
    events = epoll.poll(1)
    for fileno, event in events:
        if fileno == serversocket.fileno():
            connection, address = serversocket.accept()
            connection.setblocking(0)
            epoll.register(connection.fileno(), select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            responses[connection.fileno()] = response
        elif event & select.EPOLLIN:
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                epoll.modify(fileno, select.EPOLLOUT)
                print('-'*40 + '\n' + requests[fileno].decode()[:-2])
        elif event & select.EPOLLOUT:
            byteswritten = connections[fileno].send(responses[fileno])
            responses[fileno] = responses[fileno][byteswritten:]
            if len(responses[fileno]) == 0:
                epoll.modify(fileno, 0)
                connections[fileno].shutdown(socket.SHUT_RDWR)
        elif event & select.EPOLLHUP:
            epoll.unregister(fileno)
            connections[fileno].close()
            del connections[fileno]
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

# (client_socket, address) = serversocket.accept()
# print('Connected to client')

# print('Relaying data')
# start = timeit.default_timer()

# while True:
#     file_chunk = client_socket.recv(FILE_CHUNK_SIZE)

#     if file_chunk == "":
#         break

#     socket1.send(file_chunk)
#     socket2.send(file_chunk)
#     socket3.send(file_chunk)

# end = timeit.default_timer()
# print('Send file completed. Time: ' + str(end - start))




