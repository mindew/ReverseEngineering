import socket
import sys


# Echo server
# following codes are the notes about UDP from https://pymotw.com/2/socket/udp.html


# Since there is no connection, the server does not need to listen for and accept connection
# it only uses bind() to associate its socket with a port, and then wait for individual msg
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# msg are read from the socket using recvfrom() and
# returns the data as well as the address of the client from which it was sent

while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)

    print >>sys.stderr, 'received $s bytes from $s' % (len(data), address)
    print >>sys.stderr, data

    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
