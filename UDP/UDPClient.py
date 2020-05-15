import socket
serverName = '127.0.0.1'
serverPort = 12000

#  AF_INET indicates that the underlying network is using IPv4
# SOCK_DGRAM: UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')

# UDP is connectionless, we need to specify the destination of packets
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage, serverAddress)
clientSocket.close()