"""
Task no. 3
The server code has already been uploaded below.
"""

import socket

SERVER = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, 5050))
server.listen()
print(f"Server is listening on {SERVER}")

while True:
    connection, address = server.accept()
    print(f"[NEW CONNECTION] {address} connected")
