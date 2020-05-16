import socket

serverPort = 11000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(10)

print("the server 1 is ready")
while 1:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(2048)
    response = "HTTP/1.1 200 OK\n" \
    +"Content-Type: text/html\n" \
    +"\n" \
    +"<html><body>Hello from server 1</body></html>\n"
    connectionSocket.send(response.encode())
    connectionSocket.close()

serverSocket.close()