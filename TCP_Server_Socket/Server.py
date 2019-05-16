from socket import *

if __name__ == '__main__':
    HOST = ''
    PORT = 10000
    BUF_SIZE = 1024
    ADDRESS = (HOST, PORT)

    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(ADDRESS)
    tcp_server_socket.listen(5)

    while True:
        print('waiting for connection...')
        tcp_client_socket, client_address = tcp_server_socket.accept()
        print('connected from: ', client_address)

        while True:
            data = tcp_client_socket.recv(BUF_SIZE)
            if not data:
                break
            tcp_client_socket.send(data)
        tcp_client_socket.close()
