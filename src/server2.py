"""Updated server.py script from WK 2 Day 9 Lecture notes, the changes here make the server function a Non-blocking one."""

import socket
import select
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    print('Socket bind is complete.')
    server_socket.listen(5)
    print('Socket is now listening....stop shouting...')
    print('<Ctrl> + C to exit')
    buffsize = 79

    input = [server_socket, sys.stdin]
    running = True

    try:
        while running:

            read_ready, wrrite_ready, except_ready = select.select(input, [], [], 0)

            for readable in read_ready:

                if readable is server_socket:
                    # spin up new handler sockets as clients connect
                    handler_socket, address = readable.accept()  # won't block now
                    input.append(handler_socket)

                elif readable is sys.stdin:
                    # handle any stdin by terminating the server
                    sys.stdin.readline()
                    running = False
                else:
                    # handle each client connectino 1 buffer at a time
                    data = readable.recv(buffsize)  # also won't block
                    if data:
                        # return one buffer's worth of mesage to the client
                        readable.sendall(b'\nClient message recieved, echoing back!\n')
                        readable.sendall(data)
                        print(readable)
                        print('readable is above ^')
                        print('\nSocket still listening.')
                    else:
                        readable.close()
                        input.remove(readable)
    except KeyboardInterrupt:
        server_socket.close()
        print("Socket is Closed, suckuh.")


if __name__ == '__main__':
    server()
