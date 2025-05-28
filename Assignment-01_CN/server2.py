import random, time
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

while True:
    
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    print("Packet received successfully")
    message = message.decode()
    message= float(message)
    cal_time = time.time() - message
    print(f"time difference: {cal_time}")
    
    if rand < 4:
        continue
    message = str(message)
    serverSocket.sendto(message.encode(), address)