import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

while True:
    message = input('Ingrese un mensaje: ')
    client_socket.send(message.encode())
    print(client_socket.recv(1024).decode())