import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# assign the port 12000 to the server's socket
serverSocket.bind(('', serverPort))

print("the server is ready")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(clientAddress)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    break
serverSocket.close()