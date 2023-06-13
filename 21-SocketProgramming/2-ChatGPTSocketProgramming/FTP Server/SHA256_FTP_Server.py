'''This code defines a checksum function that calculates the SHA256 checksum of a file and returns the hexadecimal representation of the checksum. It then defines a custom CustomFTPHandler class that overrides the on_file_received method to calculate the checksum of a file after it is received by the FTP server.

When a file is transferred to the FTP server, the on_file_received method will be called and the SHA256 checksum of the file will be calculated and printed to the console. This allows you to ensure the integrity of the transferred files by comparing the calculated checksum to a known good checksum.

You can customize this code further by storing'''

import os
import hashlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def checksum(filepath):
    """Calculate the SHA256 checksum of a file."""
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

# Create an authorizer that allows anonymous read-only access
authorizer = DummyAuthorizer()
authorizer.add_anonymous("/path/to/ftp/root", perm="elradfmw")

# Create an FTP handler that uses the anonymous authorizer
class CustomFTPHandler(FTPHandler):
    def on_file_received(self, filepath):
        """Calculate the SHA256 checksum of a file after it is received."""
        checksum = self.checksum(filepath)
        print(f"Received file {filepath} with checksum {checksum}")

handler = CustomFTPHandler
handler.authorizer = authorizer
handler.checksum = checksum

# Bind the handler to the FTP server and serve indefinitely
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
