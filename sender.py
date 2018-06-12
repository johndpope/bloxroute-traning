import sys
import socket
import timeit

FILE_CHUNK_SIZE = 80000

file_name, ip, port = sys.argv[1], sys.argv[2], int(sys.argv[3])

print('Opening connection to server')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((ip, port))

def send_file(p_socket, p_file_name):
    print('Sending file')
    start = timeit.default_timer()
    
    with open(p_file_name, 'r') as file:
        file_chunk = file.read(FILE_CHUNK_SIZE)
        
        while file_chunk != '':
            file_chunk = file.read(FILE_CHUNK_SIZE)
            p_socket.send(file_chunk)
    
    end = timeit.default_timer()
    print('Send file completed. Time: ' + str(end - start))

send_file(socket, file_name)



