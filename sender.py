import sys
import socket
import timeit
import select


FIRST_CHUNK_SIZE = 1024
FILE_CHUNK_SIZE = 80000

file_name = sys.argv[1]
ip1, port1 = sys.argv[2], int(sys.argv[3])

print('Opening connection to relay')
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((ip1, port1))

print('Sending file')
start = timeit.default_timer()

with open(file_name, 'r') as file:
    file_chunk = file.read(FILE_CHUNK_SIZE)
    socket1.send(file_chunk)

    while file_chunk != '':
        file_chunk = file.read(FILE_CHUNK_SIZE)
        socket1.send(file_chunk)

end = timeit.default_timer()
print('Send file completed. Time: ' + str(end - start))



