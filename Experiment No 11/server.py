import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()

        try:
            print('Connection from', client_address)

            # Send data
            message = 'Hello, client! You are connected.'
            client_socket.sendall(message.encode('utf-8'))

        finally:
            # Clean up the connection
            client_socket.close()

if __name__ == '__main__':
    start_server()