import sockets
import threading

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

# list of clients
clients = []

def handle_client(client_socket):
    # get client name
    name = client_socket.recv(1024).decode('ascii')

    # send a welcome message
    welcome_msg = 'Welcome %s to the server room\r\n' % name
    client_socket.send(welcome_msg.encode('ascii'))

    # add client to the list
    clients.append(client_socket)

    # notify other clients
    broadcast(bytes('%s has joined the server room.\r\n' % name, 'ascii'), client_socket)

    while True:
        try:
            # receive message from client
            msg = client_socket.recv(1024)

            if msg == bytes('quit', 'ascii'):
                # remove client from the list
                clients.remove(client_socket)

                # notify other clients
                broadcast(bytes('%s has left the server room.\r\n' % name, 'ascii'), client_socket)
                break

            else:
                # broadcast message to other clients
                broadcast(msg, client_socket)

        except:
            # remove client from the list
           
