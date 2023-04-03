import socket

def openchatbox():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect(("127.0.0.1", 8080))
        message = str(input("Enter message: "))
        mysocket.send(f"{message}".encode())
        mysocket.close()

if __name__ == '__main__':
    openchatbox()