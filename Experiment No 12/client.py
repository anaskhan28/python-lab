import socket

def start_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address
    server_address = ('localhost', 12345)

    try:
        # Send data
        message = 'Hello, server! This is the client.'
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Receive response
        data, server = client_socket.recvfrom(4096)
        print('UDP Received message from server:', data.decode('utf-8'))

    finally:
        client_socket.close()

if __name__ == '__main__':
    start_client()