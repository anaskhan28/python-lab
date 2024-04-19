import socket

def start_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    while True:
        print('\nWaiting to receive message...')
        data, address = server_socket.recvfrom(4096)

        print('UDP Received message from client:', data.decode('utf-8'))
        print('Client IP Address:', address)

        # Send data
        message = 'Hello, client! You received my message.'
        server_socket.sendto(message.encode('utf-8'), address)

if __name__ == '__main__':
    start_server()