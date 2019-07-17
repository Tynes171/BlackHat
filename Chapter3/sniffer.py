import socket
import os, argparse



ap = argparse.ArgumentParser()

ap.add_argument("-a", "--address", default="127.0.0.1", help="Host IP")

args = ap.parse_args()

host = args.address

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP

else:
    socket_protocol = socket.IPPROTO_ICMP


sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))


sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)


if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


print sniffer.recvfrom(65565)


if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
