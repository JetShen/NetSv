import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print('Servidor escuchando en localhost: 8080')

    client_sockets = []

    while True:
        client_socket, address = server_socket.accept()
        client_sockets.append(client_socket)

        print(f'Conexión establecida desde {address}')

        for c in client_sockets:
            if c is not client_socket:
                message = client_socket.recv(1024)
                c.send(message)

    server_socket.close()

if __name__ == '__main__':
    start_server()
