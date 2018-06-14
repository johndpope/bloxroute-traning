import sys
import socket, select
import timeit
import select

FIRST_CHUNK_SIZE = 1024
FILE_CHUNK_SIZE = 80000

file_name = sys.argv[1]
ip1, port1 = sys.argv[2], int(sys.argv[3])

print('Opening connection to relay')
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((ip1, port1))
socket1.setblocking(0)

print('Starting epoll')
epoll = select.epoll()
epoll.register(socket1.fileno(), select.EPOLLOUT | select.EPOLLHUP| select.EPOLLET)


print('Sending file')
start = timeit.default_timer()

send_completed = False
file_chunk = None

try:
    connections = {}
    with open(file_name, 'r') as file:
        file_chunk = None
        bytes_sent = 0

        while True:
            if send_completed:
                print('Finished sending')
                break

            events = epoll.poll(-1)
            for fileno, event in events:
                if event & select.EPOLLOUT:
                    try:
                        while True:
                            file_chunk = file.read(FILE_CHUNK_SIZE)

                            if file_chunk == "":
                                send_completed = True
                                break
                            
                            bytes_sent = socket1.send(file_chunk)
                    except socket.error:
                        pass

                elif event & select.EPOLLHUP:
                    epoll.unregister(fileno)
                    connections[fileno].close()
                    del connections[fileno]
finally:
    epoll.unregister(socket1.fileno())
    epoll.close()
    socket1.close()

end = timeit.default_timer()
print('Send file completed. Time: ' + str(end - start))