import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 9999

# Bind the socket to a public host, and a port
s.bind((host, port))

# Become a server socket
s.listen(1)

print("Waiting for a connection...")

# Accept connections from multiple clients
clients = {}
while True:
    conn, addr = s.accept()
    print("Connection from", addr)
    # Receive the client's name
    name = conn.recv(1024).decode()
    clients[name] = conn
    print(f"{name} has joined the chat")
    # Send a message to all clients to inform them of the new user
    message = f"{name} has joined the chat"
    for client in clients.values():
        client.sendall(message.encode())
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # Parse the message to determine the recipient and the message
        try:
            recipient, message = data.decode().split(":", 1)
        except ValueError:
            # If the message is invalid, just skip it
            continue
        # If the recipient is 'all', send the message to all clients
        if recipient == "all":
            for client in clients.values():
                client.sendall(data)
        # Otherwise, send the message only to the specified recipient
        elif recipient in clients:
            clients[recipient].sendall(data)
    # Remove the client from the list
    del clients[name]
    print(f"{name} has left the chat")
    # Send a message to all clients to inform them of the user leaving
    message = f"{name} has left the chat"
    for client in clients.values():
        client.sendall(message.encode())
    conn.close()
