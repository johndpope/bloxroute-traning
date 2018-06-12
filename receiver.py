import sys
import socket
import timeit

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

buffer = bytearray(BUFFER_SIZE)
memview = memoryview(buffer)
total_bytes_received = 0

while True:
    bytes_count = client_socket.recv_into(memview, BUFFER_SIZE)
    if bytes_count == 0:
        break
    total_bytes_received += bytes_count

end = timeit.default_timer()
print('Received the file. Time: ' + str(end - start) + '. Bytes: ' + str(total_bytes_received))

# print('Saving file')
# with open('output.txt', 'w') as f:
#     nwritten = 0
#     while nwritten < total_bytes_received:
#         f.write(bytes(memview[nwritten:nwritten + BUFFER_SIZE]))
#         nwritten += BUFFER_SIZE
# print('Saved file')