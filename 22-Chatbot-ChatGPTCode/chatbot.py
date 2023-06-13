import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 9999

# Connect to the server
s.connect((host, port))

# Send a message to the server
message = "Hello, World!"
s.sendall(message.encode())

# Receive data from the server
data = s.recv(1024)

# Close the connection
s.close()

print("Received", repr(data))
