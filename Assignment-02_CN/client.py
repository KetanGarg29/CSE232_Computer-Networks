#python3 client.py localhost 6786 HelloWorld.html
import socket
server_name = 'localhost'  
server_port = 6786 

socket_of_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_of_client.connect((server_name, server_port))

messages = "GET /HelloWorld.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
messages= messages.encode()
socket_of_client.send(messages)

repo= b""
while(True):
    output = socket_of_client.recv(4096)

    if  not output  :
        break
    
    repo+=output

print(repo.decode())

socket_of_client.close()