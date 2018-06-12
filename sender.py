import sys
import socket
import timeit

FILE_CHUNK_SIZE = 80000

file_name, ip, port = sys.argv[1], sys.argv[2], int(sys.argv[3])

print('Opening connection to server')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, port))

print('Sending file')
start = timeit.default_timer()

with open(file_name, 'r') as file:
    file_chunk = file.read(FILE_CHUNK_SIZE)
    
    while file_chunk != '':
        file_chunk = file.read(FILE_CHUNK_SIZE)
        socket.send(file_chunk)

end = timeit.default_timer()
print('Send file completed. Time: ' + str(end - start))



