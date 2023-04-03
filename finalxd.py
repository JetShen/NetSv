import socket



def start_server():
    first = True
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 80))
    server_socket.listen(1)
    print('Servidor escuchando en localhost: 80')

    while True:
        client_socket, address = server_socket.accept()
        if first:
            print(f'Conexión establecida desde {address}')
            first = False
        
        message = client_socket.recv(1024)
        print(f'Mensaje recibido: {message.decode()}')
        if message.decode() == 'close':
            return False
        
        if message.decode() == 'show address':
            print(f'Conexión establecida desde {address}')
        
        client_socket.close()

if __name__ == '__main__':
    start_server()