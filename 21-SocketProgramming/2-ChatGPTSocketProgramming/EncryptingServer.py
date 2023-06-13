import socket
import base64
from Crypto.Cipher import AES

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

# The secret key must be shared between the sender and the receiver
# It is recommended to use a key with 32 bytes (256 bits)
SECRET_KEY = b'0123456789abcdef0123456789abcdef'

def encrypt(message):
    # Padding is added to the message to ensure that it is a multiple of 16 bytes
    message = message.encode()
    padding = b' ' * (AES.block_size - len(message) % AES.block_size)
    message += padding
    # Create a cipher object using the secret key
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    # Encrypt the message
    encrypted_message = cipher.encrypt(message)
    # Encode the encrypted message in base64 for easy transmission
    # over the network
    return base64.b64encode(encrypted_message).decode()

def decrypt(encrypted_message):
    # Decode the encrypted message from base64
    encrypted_message = base64.b64decode(encrypted_message)
    # Create a cipher object using the secret key
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)
    # Decrypt the message
    message = cipher.decrypt(encrypted_message)
    # Remove the padding
    return message.rstrip().decode()

while True:
    conn, addr = s.accept()
    print("Connection from", addr)
    # Receive the client's name
    name = conn.recv(1024).decode()
    clients[name] = conn
    print(f"{name} has joined the chat")
    # Send a message to all clients to inform them of the new user
    message = f"{name} has joined the chat"
    message = encrypt(message)
    for client in clients.values():
        client.sendall(message.encode())
    while True:
        data = conn.recv(1024)