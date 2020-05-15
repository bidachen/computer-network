import socket

#  With TCP, all bytes sent from one side not are not only guaranteed to arrive at the other side 
#  but also guaranteed arrive in order

serverPort = 12000

# a welcome socket used to connect with a client
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))

# maximum number of queued connections is 1
serverSocket.listen(1)

print("the server is ready")
while 1:
    # connection socket used to send packets
    connectionSocket, addr = serverSocket.accept()
    print(addr)
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
    break
serverSocket.close()