"""Server module that creates a local server."""

import socket


def server():
    """Open a local server in the command line."""
    server_sock = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM
                                socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server_sock.bind(address)
    print('Socket bind is completely complete.')
    server_sock.listen(1)
    print('Socket is now listening....spooky')
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        while True:
            conn, addr = server_sock.accept()
            buffer_length = 79
            message_complete = False
            return_message = ' '
            while not message_complete:
                part = conn.recv(buffer_length)
                print(part.decode('utf-8'))
                if len(part) < buffer_length:
                    message_complete = True
                return_message += part.decode('utf-8')
            print(return_message)
            conn.sendall(return_message.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    server()
