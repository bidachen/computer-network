import socket
serverName = '127.0.0.1'
serverPort = 12000

# AF_INET: IPv4
# SOCK_STREAM: TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TCP: need 3-way-handshake connection before sending packets
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence:')

# have connected to server already, no need to attach server's information
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())
clientSocket.close()