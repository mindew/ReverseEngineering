import socket
import sys


# Echo client
# following codes are the notes about UDP from https://pymotw.com/2/socket/udp.html
# UDP echo client does not use bind to attach its socket to an address.
# IT uses sendto() to deliver and recvfrom() to receive the response

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message. It will be repeated'

try:

    # send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
