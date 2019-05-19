from socket import *

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 10000
    BUF_SIZE = 1024
    ADDRESS = (HOST, PORT)

    udp_client_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = input('> ')
        if not data:
            break
        udp_client_socket.sendto(bytes(data, encoding='utf8'), ADDRESS)
        data, server_address = udp_client_socket.recvfrom(BUF_SIZE)
        if not data:
            break
        print(data)
