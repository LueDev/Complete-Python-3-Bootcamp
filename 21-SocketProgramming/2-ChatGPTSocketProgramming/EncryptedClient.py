import socket
import base64
from Crypto.Cipher import AES

# The secret key must be the same as the one used by the server
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

# Create a socket object
