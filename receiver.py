import sys
import socket, select
import timeit
from collections import deque

BUFFER_SIZE = 80000

ip, port = sys.argv[1], int(sys.argv[2])

print('Open socket listener')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((ip, port))
serversocket.listen(5)
serversocket.setblocking(0)
print('Socket connection opened successfully')

print('Starting epoll')
epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN | select.EPOLLET)

buffer = deque()
total_bytes_received = 0
start = None

try:
    connections = {}; requests = {}; responses = {}
    while True:
        print('Waiting for events on the socker')
        events = epoll.poll(-1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                try:
                    while True:
                        connection, address = serversocket.accept()
                        connection.setblocking(0)
                        epoll.register(connection.fileno(), select.EPOLLIN | select.EPOLLET)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = response
                except socket.error:
                    pass
            elif event & select.EPOLLIN:
                try:
                    if start == None:
                        start = timeit.default_timer()

                    while True:
                        new_bytes += connections[fileno].recv(1024)
                        buffer.append(new_bytes)
                        total_bytes_received += len(new_bytes)
                except socket.error:
                    pass
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

end = timeit.default_timer()

print('Received the file. Time: ' + str(end - start) + '. Bytes: ' + str(total_bytes_received))

# (client_socket, address) = serversocket.accept()
# print('Connected to client')

# print('Start receiving file')

# buffer = deque()
# total_bytes_received = 0
# start = None

# while True:
#     rcvd_bytes = client_socket.recv(BUFFER_SIZE)
#     if start == None:
#         start = timeit.default_timer()

#     if rcvd_bytes == "":
#         break
#     buffer.append(rcvd_bytes)
#     total_bytes_received += len(rcvd_bytes)
# end = timeit.default_timer()
# print('End time ' + str(end))
# print('Received the file. Time: ' + str(end - start) + '. Bytes: ' + str(total_bytes_received))


# print('Saving file')
# with open('output.txt', 'w') as f:
#     f.write(buffer[0:total_bytes_received])
# print('Saved file')
