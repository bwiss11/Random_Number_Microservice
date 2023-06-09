# Author: Blaine Wissler
# Date: May 5, 2023
# Modified from template code taken from: https://realpython.com/python-sockets/


import random
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            rand_number = str((random.randint(1,10000)))
            if not data:
                break
            # Encodes to utf-8 and sends to the client
            conn.sendall(rand_number.encode())

