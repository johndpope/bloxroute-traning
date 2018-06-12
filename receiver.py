import sys
import socket

ip, port = sys.argv[1], int(sys.argv[2])

print('Open socket listener')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((ip, port))
serversocket.listen(5)
print('Socket connection opened successfully')

(clientsocket, address) = serversocket.accept()

print('Connected to client')

chunks = bytearray(0)

while True:
    chunk = clientsocket.recv(1024)
    if chunk == '':
        break
    chunks += chunk

print('Received the file')

with open('output.txt', 'w') as f:
    read_data = f.write(chunks)