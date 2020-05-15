import socket

def parseRequest(request):
    request = request.split(' ')
    return request[1][1:]
    
def readFile(fileName):
    f = open(fileName, 'rb')
    fileData = f.read()
    f.close()
    return fileData

serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print("the server is ready")
while 1:
    connectionSocket, addr = serverSocket.accept()
    request = connectionSocket.recv(2048)
    
    try:
        fileName = parseRequest(request.decode())
        fileData = readFile(fileName)
        fileLen = len(fileData)
        response = "HTTP/1.1 200 OK\n" \
        +'Content-Disposition: attachment; filename="test.txt"\n' \
        +"Content-Type: application/force-download\n" \
        +"Content-length: " + str(fileLen) + "\n" \
        +"\n"
        connectionSocket.send(response.encode())
        connectionSocket.send(fileData)
    
    except IOError:
        errorResponse = "HTTP/1.1 404 Not Found\n" \
         +"Content-Type: text/html\n" \
         +"\n" \
         +"<html><body>File Not Found</body></html>\n"
        connectionSocket.send(errorResponse.encode())
    
    connectionSocket.close()
    break

serverSocket.close()