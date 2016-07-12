"""Client script to open client server."""

import socket
import sys


def client(msg):
    """Open client server to send a message."""
    #  address changed to 10000 for server2.py
    infos = socket.getaddrinfo('127.0.0.1', 10000)
    stream_info = [idx for idx in infos if idx[1] == socket.SOCK_STREAM][0]
    client_msg = socket.socket(*stream_info[:3])
    client_msg.connect(stream_info[-1])
    client_msg.sendall(msg.encode('utf8'))
    buffer_length = 80
    msg_complete = False
    msg = u''
    while not msg_complete:
        part = client_msg.recv(buffer_length)
        msg += part.decode('utf8')
        if len(part) < buffer_length:
            msg_complete = True
        client_msg.close()
        return msg
        print(msg)


if __name__ == '__main__':
    msg = sys.argv[1]
    print(client(msg))
