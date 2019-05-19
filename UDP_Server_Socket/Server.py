from socket import *

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 10000
    BUF_SIZE = 1024
    ADDRESS = (HOST, PORT)

    udp_server_socket = socket(AF_INET, SOCK_DGRAM)
    udp_server_socket.bind(ADDRESS)

    while True:
        print('waiting for message...')
        msg, client_address = udp_server_socket.recvfrom(BUF_SIZE)
        print('msg: %s, address: %s' % (msg, client_address))

        udp_server_socket.sendto(msg, client_address)
