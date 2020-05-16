import socket, threading
from random import randrange

# simple web proxy server which redirect the http request to one of the servers

serverPort = 10000

proxySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
proxySocket.bind(('', serverPort))

print("the proxy server is ready")

server1 = ('127.0.0.1', 11000)
server2 = ('127.0.0.1', 12000)

class newThread(threading.Thread):
    def __init__(self, request, connectionSocket, counter):
        threading.Thread.__init__(self)
        self.request = request
        self.connectionSocket = connectionSocket
        self.counter = counter
    def run(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.counter == 0:
            clientSocket.connect(server1)
        else:
            clientSocket.connect(server2)
        clientSocket.send(self.request)
        response = clientSocket.recv(2048)
        clientSocket.close()
        self.connectionSocket.send(response)
        self.connectionSocket.close()
while 1:
    proxySocket.listen(1)
    connectionSocket, addr = proxySocket.accept()
    request = connectionSocket.recv(2048)
    thread = newThread(request, connectionSocket, randrange(2))
    thread.start()

proxySocket.close()