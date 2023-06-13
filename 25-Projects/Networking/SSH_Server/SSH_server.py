
'''This code imports the paramiko library and creates an SSHServer object using the SSHServer class. 
The SSHServer class is a high-level class that provides a convenient interface for creating an SSH server.'''
import paramiko

# Create an SSH server
server = paramiko.Transport(('0.0.0.0', 22))

'''This code sets the host key of the server using the add_host_key method of the SSHServer object. 
The host key is a unique key that identifies the server and is used to establish an encrypted 
connection with the client. In this case, a new RSA key is generated using the RSAKey.generate method 
of the paramiko.RSAKey class, with a key length of 2048 bits.'''
# Set the host key
server.add_host_key(paramiko.RSAKey.generate(2048))


'''This code enables public key, password, and none authentication methods using the auth_publickey, 
auth_password, and auth_none attributes of the SSHServer object, respectively. These attributes specify 
the types of authentication that the server allows.'''
# Set the authentication methods
server.auth_publickey = True
server.auth_password = True
server.auth_none = True

'''The public_key_callback function is a callback function that is called when a client attempts to 
authenticate using a public key. It takes the client's username and the public key as input, and it 
returns an authentication result.

The public_key_callback function checks if the public key is authorized by comparing it to the 
AUTHORIZED_PUBLIC_KEY variable. If the public key is authorized, the function returns paramiko.AUTH_SUCCESSFUL, 
which indicates that the authentication is successful. Otherwise, the function returns paramiko.AUTH_FAILED, 
which indicates that the authentication has failed.
'''
# Set the callback functions for authentication
def public_key_callback(username, public_key):
    # Check if the public key is authorized
    if public_key == AUTHORIZED_PUBLIC_KEY:
        return paramiko.AUTH_SUCCESSFUL
    else:
        return paramiko.AUTH_FAILED

'''The password_callback function is a callback function that is called when a client attempts to 
authenticate using a password. It takes the client's username and the password as input, and it 
returns an authentication result.

The password_callback function checks if the password is correct by comparing it to the CORRECT_PASSWORD 
variable. If the password is correct, the function returns paramiko.AUTH_SUCCESSFUL, which indicates that the authentication is successful. Otherwise, the function returns paramiko.AUTH_FAILED, which indicates that the authentication has failed.'''
def password_callback(username, password):
    # Check if the password is correct
    if password == CORRECT_PASSWORD:
        return paramiko.AUTH_SUCCESSFUL
    else:
        return paramiko.AUTH_FAILED


'''The public_key_auth_callback and password_auth_callback attributes of the SSHServer object are set to 
the public_key_callback and password_callback functions, respectively, to specify the callback functions 
for public key and password authentication.'''
server.public_key_auth_callback = public_key_callback

'''The public_key_auth_callback and password_auth_callback attributes of the SSHServer object are set to the
public_key_callback and password_callback functions, respectively, to specify the callback functions for 
public key and password authentication.'''
server.password_auth_callback = password_callback

'''This code sets the port number for the server using the bind method of the SSHServer object, and 
starts the server using the start method. The server will listen for incoming connections on the specified port.'''
# Set the port and start the server
server.bind(22)
server.start()

'''This code waits for the server to stop using the wait method of the SSHServer object. The wait 
method blocks the program execution until the server is stopped, either manually or due to an error.'''
# Wait for the server to stop
server.wait()

'''This code closes the server using the close method of the SSHServer object. The close method 
releases the resources held by the server, such as sockets and threads, and prepares the server for 
garbage collection.'''
# Close the server
server.close()