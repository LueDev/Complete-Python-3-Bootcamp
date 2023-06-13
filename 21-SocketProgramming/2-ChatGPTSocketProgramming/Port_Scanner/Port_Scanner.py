'''This code defines a port_scanner function that uses the socket library to scan a single port on a host. 
It creates a socket and uses the connect_ex method to try to connect to the port. If the connection is 
successful, the port is considered open; otherwise, it is considered closed.

The code also defines a scan_ports function that scans a range of ports on a host by calling the 
port_scanner function for each port.

This is a very simple example of a port scanner in Python, but it should give you an idea of how 
to use the socket library to scan ports on a host. You can customize the scanner by scanning 
different ranges of ports, adjusting the timeout, and performing other tasks as needed.'''

import socket

def port_scanner(host, port):
    """Scan a single port on a host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            #print(f"Port {port}: CLOSED")
            pass
        sock.close()
    except Exception as e:
        print(e)

def scan_ports(host):
    """Scan a range of ports on a host."""
    for port in range(1, 65535):
        port_scanner(host, port)

scan_ports('127.0.0.1')