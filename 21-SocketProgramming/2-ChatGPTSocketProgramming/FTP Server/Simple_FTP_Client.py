'''To create a client that can connect to an FTP server, you can use the ftplib module in Python. 
The ftplib module provides a set of functions that allow you to connect to an FTP server, list the 
files and directories on the server, download files, and upload files.

Here is an example of how you can use the ftplib module to create a simple FTP client that can list 
the files and directories on the server and download a file:'''

import ftplib

def list_files(ftp):
    files = ftp.nlst()
    for i, f in enumerate(files):
        print(f'{i+1}: {f}')

def download_file(ftp, file):
    with open(file, 'wb') as f:
        ftp.retrbinary(f'RETR {file}', f.write)

def main():
    ftp = ftplib.FTP('ftp.example.com')
    ftp.login('username', 'password')

    print('Files:')
    list_files(ftp)

    file_index = int(input('Enter the file number to download: '))
    file = ftp.nlst()[file_index - 1]

    download_file(ftp, file)
    print(f'Successfully downloaded {file}')

if __name__ == '__main__':
    main()


'''This code creates an FTP connection to the server using the FTP constructor, logs in 
using the login method, lists the files in the current directory using the nlst method, 
and allows the user to choose a file to download by entering the file number. The chosen 
file is then downloaded using the retrbinary method.

You can modify this code to add additional functionality, such as uploading files or 
navigating the directory tree on the server. For more information on the ftplib module 
and the available functions, you can refer to the Python documentation.'''