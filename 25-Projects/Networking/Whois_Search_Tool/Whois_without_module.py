'''Here is an example of how you can modify the code to perform a WHOIS lookup 
for a domain using the socket library and the WHOIS protocol:'''

import socket

'''This code imports the socket library and defines a whois_lookup function that takes a 
domain name as an argument. It then uses the create_connection function from the socket 
library to connect to a WHOIS server at whois.verisign-grs.com on port 43. The WHOIS protocol 
uses port 43 for communication, and whois.verisign-grs.com is a well-known WHOIS server that 
can be used to look up information for many top-level domains (TLDs) such as .com and .net.'''

def whois_lookup(domain):
    """Perform a WHOIS lookup for a domain using the WHOIS protocol."""
    # Connect to the WHOIS server
    sock = socket.create_connection(('whois.verisign-grs.com', 43))

    '''This code sends the domain name to the WHOIS server using the send method. The domain 
    name is sent as a string, with a line break (\r\n) at the end to signal the end of the request. 
    The string is encoded as a byte string using the encode method before it is sent to the server.'''
    # Send the domain name to the server
    sock.send(f"{domain}\r\n".encode('utf-8'))

    '''This code receives and prints the WHOIS information from the server using the recv method. 
    The recv method reads up to 4096 bytes of data from the server and returns it as a byte string. 
    The byte string is then decoded as a Unicode string using the decode method and printed to the console.'''
    # Receive and print the WHOIS information
    response = sock.recv(4096).decode('utf-8')
    print(response)

    # Close the connection
    sock.close()

whois_lookup('example.com')

'''
This is the complete code for a simple WHOIS search tool in Python that uses the WHOIS protocol 
to perform a WHOIS lookup for a domain. It connects to a WHOIS server, sends a request for the 
WHOIS information for a domain, receives and prints the response from the server, and then closes 
the connection. You can customize the tool by connecting to different WHOIS servers, parsing the 
WHOIS information, and performing other tasks

This code uses the create_connection function from the socket library to connect to a WHOIS 
server at whois.verisign-grs.com on port 43. It then sends the domain name to the server using 
the send method and receives and prints the WHOIS information using the recv method. Finally, 
it closes the connection using the close method.

This is a very simple example of a WHOIS search tool in Python that uses the WHOIS protocol, 
but it should give you an idea of how to perform a WHOIS lookup for a domain without using a 
third-party library. You can customize the tool by connecting to different WHOIS servers, 
parsing the WHOIS information, and performing other tasks as needed.'''