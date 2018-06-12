import sys
import socket
import timeit

FILE_CHUNK_SIZE = 80000

file_name = sys.argv[1]
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

print('Sending file')
start = timeit.default_timer()

with open(file_name, 'r') as file:
    file_chunk = file.read(FILE_CHUNK_SIZE)
    socket1.send(file_chunk)
    socket2.send(file_chunk)
    socket3.send(file_chunk)

    while file_chunk != '':
        file_chunk = file.read(FILE_CHUNK_SIZE)
        socket1.send(file_chunk)
        socket2.send(file_chunk)
        socket3.send(file_chunk)

end = timeit.default_timer()
print('Send file completed. Time: ' + str(end - start))



