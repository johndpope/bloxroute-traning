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

(clientsocket, address) = serversocket.accept()
print('Connected to client')

def receive_file(client_socket):
    
    print('Start receiving file')
    start = timeit.default_timer()

    buffer = bytearray(BUFFER_SIZE)
    memview = memoryview(buffer)
    
    while True:
        bytes_count = client_socket.recv_into(memview, BUFFER_SIZE)
        if bytes_count == 0:
            break
    
    end = timeit.default_timer()
    print('Received the file. Time: ' + str(end - start))

receive_file(clientsocket)