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
epoll.register(serversocket.fileno(), select.EPOLLIN | select.EPOLLHUP| select.EPOLLERR | select.EPOLLET)

buffer = deque()
total_bytes_received = 0
start = None
new_bytes = None
finished_receiving = False

try:
    connections = {}
    while True:
        if finished_receiving:
            print('Ending epoll loop')
            break

        events = epoll.poll(-1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                try:
                    while True:
                        connection, address = serversocket.accept()
                        connection.setblocking(0)
                        epoll.register(connection.fileno(), select.EPOLLIN | select.EPOLLHUP | select.EPOLLET)
                        connections[connection.fileno()] = connection
                except socket.error as e:
                    pass
            elif event & select.EPOLLIN:
                try:
                    if start == None:
                        print('Start receiving file')
                        start = timeit.default_timer()

                    while True:
                        new_bytes = connections[fileno].recv(1024)
                        total_bytes_received += len(new_bytes)

                        if len(new_bytes) == 0:
                            print('Zero bytes received')
                            finished_receiving = True
                            break

                except socket.error:
                    pass

            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
                
                print('EPOLLHUP received')
                finished_receiving = True
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

end = timeit.default_timer()

print('Received the file. Time: ' + str(end - start) + '. Bytes: ' + str(total_bytes_received))