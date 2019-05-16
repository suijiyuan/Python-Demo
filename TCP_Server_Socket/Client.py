from socket import *

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 10000
    BUF_SIZE = 1024
    ADDRESS = (HOST, PORT)

    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    tcp_client_socket.connect(ADDRESS)

    while True:
        data = input('> ')
        if not data:
            break
        tcp_client_socket.send(bytes(data, encoding='utf8'))
        data = tcp_client_socket.recv(BUF_SIZE)
        if not data:
            break
        print(data)
