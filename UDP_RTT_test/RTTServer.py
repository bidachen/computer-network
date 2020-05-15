import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("the server is ready")
messageCount = 0
while 1:
    ping, clientAddress = serverSocket.recvfrom(2048)
    messageCount += 1
    print(messageCount, ': ', ping.decode())
    serverSocket.sendto('pong'.encode(), clientAddress)
serverSocket.close()