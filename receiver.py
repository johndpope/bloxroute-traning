import sys
import socket
import timeit
from collections import deque

BUFFER_SIZE = 80000

ip, port = sys.argv[1], int(sys.argv[2])

print('Open socket listener')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((ip, port))
serversocket.listen(5)
print('Socket connection opened successfully')

(client_socket, address) = serversocket.accept()
print('Connected to client')

print('Start receiving file')
start = timeit.default_timer()


buffer = deque()
total_bytes_received = 0

while True:
    rcvd_bytes = client_socket.recv(BUFFER_SIZE)
    if rcvd_bytes == "":
        break
    buffer.append(rcvd_bytes)
    total_bytes_received += len(rcvd_bytes)
end = timeit.default_timer()
print('End time ' + str(end))
print('Received the file. Time: ' + str(end - start) + '. Bytes: ' + str(total_bytes_received))


# print('Saving file')
# with open('output.txt', 'w') as f:
#     f.write(buffer[0:total_bytes_received])
# print('Saved file')
