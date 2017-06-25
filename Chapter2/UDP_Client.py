"""Simple UDP(User Datagram Protocol) Client: Connectionless protocol
    Minju Kang

    Delivery is not guaranteed as it is with TCP"""

import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# UDP has different socket type

# send some data
client.sendto("AAABBBCCC", (target_host, target_port))
# Because UDP is a connectionless protocol,
# there is no call to connect beforehand
# again, str will be replaced in byte type object in python3


# receive UDP data back
data, addr = client.recvfrom(4096)


print(data)
