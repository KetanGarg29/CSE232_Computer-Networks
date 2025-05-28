#http://localhost:6786/HelloWorld.html
from socket import *
socket_of_server = socket(AF_INET, SOCK_STREAM)
socket_of_server.bind(('localhost', 6786))
socket_of_server.listen(1)

while True:
    print("Ready to serve...")
    connectionSocket, addr = socket_of_server.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode('utf-8').strip("/")
        print(f"The name of file is: {filename}")
        f = open(filename)
        outputdata = f.read()
        f.close()
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('404 Not Found'.encode())
        connectionSocket.close()
socket_of_server.close()
sys.exit()