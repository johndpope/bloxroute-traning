import sys
import socket
import timeit
import select
from collections import deque

FILE_CHUNK_SIZE = 80000

listen_port = int(sys.argv[1])
ip1, port1 = sys.argv[2], int(sys.argv[3])
ip2, port2 = sys.argv[4], int(sys.argv[5])
ip3, port3 = sys.argv[6], int(sys.argv[7])

print('Opening connection to receiver 1')
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((ip1, port1))
socket1.setblocking(0)

print('Opening connection to receiver 2')
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect((ip2, port2))
socket2.setblocking(0)

print('Opening connection to receiver 3')
socket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket3.connect((ip3, port3))
socket3.setblocking(0)

print('Open socket listener')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', listen_port))
serversocket.listen(1)
serversocket.setblocking(0)

print('Starting epoll')
epoll = select.epoll()
epoll.register(socket1.fileno(), select.EPOLLOUT | select.EPOLLHUP| select.EPOLLET)
epoll.register(socket2.fileno(), select.EPOLLOUT | select.EPOLLHUP| select.EPOLLET)
epoll.register(socket3.fileno(), select.EPOLLOUT | select.EPOLLHUP| select.EPOLLET)

epoll.register(serversocket.fileno(), select.EPOLLIN | select.EPOLLHUP | select.EPOLLET)

connections = {}
connections[socket1.fileno()] = socket1
connections[socket2.fileno()] = socket2
connections[socket3.fileno()] = socket3

ready_to_send = {}
ready_to_send[socket1.fileno()] = False
ready_to_send[socket2.fileno()] = False
ready_to_send[socket3.fileno()] = False

trackers = {}
trackers[socket1.fileno()] = 0
trackers[socket2.fileno()] = 0
trackers[socket3.fileno()] = 0

finished_receiving = False

finished_sending = {}
finished_sending[socket1.fileno()] = False
finished_sending[socket2.fileno()] = False
finished_sending[socket3.fileno()] = False


buffer = bytearray()
total_bytes_received = 0
start = None
new_bytes = None

def send_data(receiver_socket):
    fileno = receiver_socket.fileno()
    
    if(ready_to_send[fileno]):
        try:
            while trackers[fileno] < len(buffer):
                bytes_sent = receiver_socket.send(buffer[trackers[fileno]:])
                trackers[fileno] += bytes_sent
        except socket.error:
            ready_to_send[fileno] = False
        finally:
            if finished_receiving and trackers[fileno] == len(buffer):
                print('Finished sending for socket ' + str(fileno))
                finished_sending[fileno] = True

def try_send_data_to_all_receivers():
    send_data(socket1)
    send_data(socket2)
    send_data(socket3)
    
try:
    while True:
        if finished_receiving and finished_sending[socket1.fileno()] and finished_sending[socket2.fileno()] and finished_sending[socket2.fileno()]:
            print('Ending epoll loop')
            break

        events = epoll.poll(1)

        for fileno, event in events:
            if fileno == serversocket.fileno():
                try:
                    while True:
                        connection, address = serversocket.accept()
                        connection.setblocking(0)
                        epoll.register(connection.fileno(), select.EPOLLIN | select.EPOLLHUP | select.EPOLLERR | select.EPOLLET )
                        connections[connection.fileno()] = connection
                        print('Connected to sender ' + str(connection.fileno()))
                except socket.error as e:
                    pass
            elif event & select.EPOLLIN:
                try:
                    if start == None:
                        print('Start receiving file')
                        start = timeit.default_timer()

                    while True:
                        new_bytes = connections[fileno].recv(1024)
                        
                        buffer += new_bytes
                        
                        if len(new_bytes) == 0:
                            print('Zero bytes received. Ended receiving.')
                            finished_receiving = True
                            break
                except socket.error as e:
                    pass
            
            elif event & select.EPOLLOUT:
                ready_to_send[fileno] = True
                send_data(connections[fileno])

            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
                
                print('EPOLLHUP received')
                finished_receiving = True

        try_send_data_to_all_receivers()
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()

end = timeit.default_timer()

print('Completed relay. Time: ' + str(end - start))



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

# socket1.close()
# socket2.close()
# socket3.close()

# serversocket.close()




