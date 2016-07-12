from __future__ import print_function

import socket
import sys


def client(msg, log=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
    )
    print('connecting to {0} port {1}'.format(*server_address), file=log)
    sock.connect(server_address)
    response = b''
    done = False
    bufsize = 16
    try:
        print('sending "{0}"'.format(msg), file=log)
        sock.sendall(msg.encode('utf8'))
        # shut the socket for writing once we are finished.  This will send a
        # 0-byte message to the server and let it know we are done.
        sock.shutdown(socket.SHUT_WR)
        while not done:
            chunk = sock.recv(bufsize)
            if len(chunk) < bufsize:
                done = True
            response += chunk
        print('received "{0}"'.format(response.decode('utf8')), file=log)
    finally:
        print('closing socket', file=log)
        sock.close()
    return response


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usg = '\nusage: python echo_client.py "this is my message"\n'
        print(usg)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
