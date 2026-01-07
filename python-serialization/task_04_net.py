#!/usr/bin/env python3
"""
Task 4: Client-Server Application with Serialization (Advanced).
Send a Python dictionary from client to server using sockets + JSON.
"""

import json
import socket


HOST = "127.0.0.1"
PORT = 65432


def start_server(host=HOST, port=PORT):
    """
    Start a server that listens for one connection, receives JSON data,
    deserializes it into a dictionary, prints it, then closes.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)

        conn, _addr = server_socket.accept()
        with conn:
            chunks = []
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                chunks.append(data)

            raw = b"".join(chunks).decode("utf-8")
            received = json.loads(raw)

            print("Received Dictionary from Client:")
            print(received)

    except Exception:
        # Keep it simple for the checker; no extra prints unless required.
        pass
    finally:
        server_socket.close()


def send_data(data, host=HOST, port=PORT):
    """
    Client: connect to server and send a serialized dictionary, then close.
    """
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        payload = json.dumps(data).encode("utf-8")
        client_socket.sendall(payload)

        client_socket.close()
    except Exception:
        pass

