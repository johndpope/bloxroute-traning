import sys
import socket
import timeit

file_name, ip, port = sys.argv[1], sys.argv[2], int(sys.argv[3])

#Open file
print('Reading file content')
file = open(file_name, 'r')
file_data = file.read()
print('Read file successfully')

#Opening the socket
print('Opening connection to server')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

print('Sending file content')

start = timeit.default_timer()
print('File transfer started')

s.send(file_data)

stop = timeit.default_timer()
print('File transfer completed')

print('Time: ' + str(stop - start)) 






