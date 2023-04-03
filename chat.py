import socket
import tkinter as tk
from threading import Thread

class Client:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cliente Chat")
        
        self.chat_box = tk.Text(self.root, state='disabled')
        self.chat_box.pack(padx=10, pady=10, fill='both', expand=True)
        
        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack(padx=10, pady=10, fill='x')
        self.message_entry.bind('<Return>', self.send_message)
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8080))
        
        self.receive_thread = Thread(target=self.receive_messages)
        self.receive_thread.start()
        
        self.root.mainloop()
        
    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode()
            self.chat_box.configure(state='normal')
            self.chat_box.insert('end', message + '\n')
            self.chat_box.configure(state='disabled')
    
    def send_message(self, event):
        message = self.message_entry.get()
        self.socket.send(message.encode())
        self.message_entry.delete(0, 'end')

if __name__ == '__main__':
    client = Client()