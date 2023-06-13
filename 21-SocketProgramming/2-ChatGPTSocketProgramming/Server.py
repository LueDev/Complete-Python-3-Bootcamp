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

# Accept a connection
conn, addr = s.accept()

print("Connection from", addr)

# Receive data from the client
data = conn.recv(1024)

# Send data to the client
message = "Thank you for connecting"
conn.sendall(message.encode())

# Close the connection
conn.close()