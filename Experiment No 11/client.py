import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        # Receive data
        data = client_socket.recv(1024)
        print('Received message from server:', data.decode('utf-8'))

    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == '__main__':
    start_client()