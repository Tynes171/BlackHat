import socket

target_host = "127.0.0.1"
target_port = 9999


#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send Some Data
client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4096)


print data


