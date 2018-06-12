import sys
import socket
import timeit

FILE_CHUNK_SIZE = 80000

listen_port = sys.argv[1]
ip1, port1 = sys.argv[2], int(sys.argv[3])
ip2, port2 = sys.argv[4], int(sys.argv[5])
ip3, port3 = sys.argv[6], int(sys.argv[7])


