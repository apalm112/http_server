"""Client script to open client server."""

import socket
import sys


def client(msg):
    """Open client server to send a message."""
    infos = socket.getaddrinfo
    stream_info = [idx for idx in infos if idx[1] == socket.SOCK_STREAM][0]
    client_msg = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client_msg.sendall(msg.encod('utf8'))
    buffer_length = 79
    msg_complete = False
    while not msg_complete:
        part = client_msg.recv(buffer_length)
        print(part.decode('utf8'))
        if len(part) < buffer_length:
            msg_complete = True
            print(msg_complete)
        client_msg.close()


if __name__ == '__main__':
    msg = sys.arg[1]
    client(msg)
