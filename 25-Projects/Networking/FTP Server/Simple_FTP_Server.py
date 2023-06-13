'''To create an FTP server in Python, you will need to use the ftplib module. Here is an 
example of how you can use this module to create a simple FTP server that lists the files 
in a directory and allows the client to choose and download a file:'''

import ftplib

def list_files(ftp):
    files = ftp.nlst()
    for i, f in enumerate(files):
        print(f'{i+1}: {f}')

def download_file(ftp, file):
    with open(file, 'wb') as f:
        ftp.retrbinary(f'RETR {file}', f.write)

def main():
    ftp = ftplib.FTP('localhost')
    #ftp.login()
    
    #you can create an anonymous login that allows clients to access a restricted set of 
    # resources without providing a username or password. To do this, you can set the 
    # user field to 'anonymous' and the password field to any email address in the login method:
    ftp.login('anonymous', 'user@example.com')
    
    #To disable authentication on the FTP server, you can set the user and 
    #password fields to empty strings in the login method:
    #ftp.login('', '')

    print('Files:')
    list_files(ftp)

    file_index = int(input('Enter the file number to download: '))
    file = ftp.nlst()[file_index - 1]

    download_file(ftp, file)
    print(f'Successfully downloaded {file}')

if __name__ == '__main__':
    main()
    
'''This code creates an FTP connection to the server and logs in using the login method. 
It then lists the files in the current directory using the nlst method and allows the 
user to choose a file to download by entering the file number. The chosen file is then 
downloaded using the retrbinary method.

Note that this is just a basic example and you will need to add additional error handling 
and functionality as needed for your specific use case.'''