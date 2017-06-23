"""Simple TCP(Transmission Control Protocol) Client
    Minju Kang

    Critical Assumptions: connection will always succeed
                          server is always expecting us to send data first
                            (as opposed to servers that expect to send data to you firsst and await your response)
                          server will always send us data back in a timely fashion

                          WORKS ONLY IN PYTHON 2"""

import socket

target_host = "www.google.com"
target_port = 80

# create a new socket object using the given address
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.socket([family[,type[proto]]])
# socket type: SOCK_STREAM(default), SOCK_DCTRAM... etc
# family: AF_INET(default), AF_INET6, AF_UNIX
# AF_INET --> saying that a standard IPv4 is gonna be used,
# SOCK_STREAM --> indicates that this is a TCP client
# protocol is usually 0 but ommitted in the line above


""" For python3:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("google.com", 80))

The socket "s" can be used to send in a request for the text of the page.
The same socket will read the reply and then be destroyed
Client sockets are normally only used for one exchange (or a small set of exchanges)
Python3 codes are referenced from https://docs.python.org/3/howto/sockets.html

For sending, python3:
    client.send(bytes[,flags])
"""


# connect the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response)
