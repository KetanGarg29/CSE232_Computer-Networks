from socket import *
import threading
def action_on_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1].decode('utf-8').strip("/")
        print(f"file to be opened: {filename}")
        f = open(filename)
        outputdata = f.read()
        f.close()
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n'.encode())
        connectionSocket.send(outputdata.encode())
    except IOError:
        connectionSocket.send('HTTP/1.0 404 Not Found\r\n\r\n'.encode())
    connectionSocket.close()  
def begin_servo(port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('localhost', port))
    serverSocket.listen(5)  
    print("Ready to serve..,")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"{addr} has connected with the server")
        client_thread = threading.Thread(target=action_on_client, args=(connectionSocket,))
        client_thread.start()

begin_servo(6786)
