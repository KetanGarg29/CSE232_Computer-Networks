import socket, time
server_address = ('127.0.0.1', 12000)
TIMEOUT = 1 
Pingstosent = 10
def stats(client_socket,server_address):
    rtts = []
    lostpackets= 0
    ping_no=1
    consec_packets=0
    while (True):
       print(f"Sending ping {ping_no}..")
       sending_time = time.time() 
       message = f"{time.time()}"
       try: 
        client_socket.sendto(message.encode(), server_address)
        response, address = client_socket.recvfrom(1024)
        rtt = time.time() - sending_time
        rtts.append(rtt)
        consec_packets=0
        print(f"RTT = {rtt:.4f} seconds")
       except socket.timeout:
        print("Request timed out")
        lostpackets+=1
        consec_packets+=1
        if consec_packets>= 3:
           print("Application stopped")
           break
       ping_no+=1    
    client_socket.close() 
    return ping_no  
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)
    ping_num = stats(client_socket,server_address)
    print("No. of times the packets were sent before applications stopped: ",ping_num - 3)
main()




