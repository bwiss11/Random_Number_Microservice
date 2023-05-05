# Author: Blaine Wissler
# Date: May 5, 2023
# Modified from template code taken from: https://realpython.com/python-sockets/

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Example request")
    data = s.recv(1024)
    num = data.decode('utf-8')

print(f"Received {num}")