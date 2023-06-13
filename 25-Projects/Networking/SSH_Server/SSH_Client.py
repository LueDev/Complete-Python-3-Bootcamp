import paramiko

# Connect to the server
client = paramiko.SSHClient()
client.connect(hostname='localhost', port=2222, username='user', password='password')

# Execute a command
stdin, stdout, stderr = client.exec_command('ls -l')

# Print the command output
print(stdout.read())

# Close the client
client.close()

'''This code creates an SSHClient object using the SSHClient class from the paramiko library, 
and uses the connect method to establish a connection with the server. The connect method takes 
the server hostname, port, username, and password as input, and it returns a tuple of stdin, stdout, 
and stderr streams. The exec_command method is then used to execute a command on the server and 
return the command output. The read method of the stdout stream is used to read the command output 
and print it to the console. Finally, the close method is used to close the client and release the 
resources held by it.'''