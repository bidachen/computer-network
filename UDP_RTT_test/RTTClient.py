import socket
import time

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    start = time.time()
    clientSocket.sendto('ping'.encode(), (serverName, serverPort))
    try:
        pong, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        print('message number ', i, ' RTT: ', end - start)
    except socket.timeout:
        print('message number ', i, ' timeout')

clientSocket.close()