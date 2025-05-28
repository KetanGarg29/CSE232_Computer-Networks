import socket, time
server_address = ('127.0.0.1', 12000)
TIMEOUT = 1 
Pingstosent = 10
def stats(client_socket,Pingstosent,server_address):
    rtts = []
    lostpackets= 0
    for ping_no in range(1, Pingstosent + 1):
       print(f"Sending ping {ping_no}..")
       sending_time = time.time() 
       message = f"Ping {ping_no} {time.time()}"
       try: 
        client_socket.sendto(message.encode(), server_address)
        response, _ = client_socket.recvfrom(1024)
        rtt = time.time() - sending_time
        rtts.append(rtt)
        print(f"Reply from server: {response.decode()} RTT = {rtt:.4f} seconds")
       except socket.timeout:
        print("Request timed out")
        lostpackets+=1
       
    client_socket.close() 
    return rtts,lostpackets   
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)
    rtts,lostpackets = stats(client_socket,Pingstosent,server_address)
    if rtts:
        print(f"\n--Ping statistics--")
        print(f"Packets sent: {Pingstosent}",f"Packets received: {len(rtts)}",f"Packets lost: {lostpackets}",f"Percentage of Packet loss: {lostpackets * 10}%")
        print(f"RTT min/avg/max = {min(rtts):.4f}/{sum(rtts) / len(rtts):.4f}/{max(rtts):.4f} seconds")
    else:
        print("No packets were sent.")
main()





