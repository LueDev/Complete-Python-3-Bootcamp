'''To create a site checker in Python, you will need to use the requests module 
to send HTTP requests to the site you want to check and the time module to 
measure the elapsed time. Here is an example of how you can use these modules 
to create a simple site checker:'''

import requests
import time

def check_site(url):
    start_time = time.time()
    try:
        r = requests.get(url)
        elapsed_time = time.time() - start_time
        if r.status_code == 200:
            print(f'Site is up! Response time: {elapsed_time:.2f} seconds')
        else:
            print(f'Site is down! Response time: {elapsed_time:.2f} seconds')
    except requests.exceptions.RequestException:
        elapsed_time = time.time() - start_time
        print(f'Site is down! Response time: {elapsed_time:.2f} seconds')

check_site('https://www.google.com')


'''This code sends an HTTP GET request to the specified URL and measures the elapsed time. 
If the request is successful (i.e., the site is up and returns a status code of 200), 
it prints a message saying the site is up along with the elapsed time. If the request 
is not successful (e.g., the site is down or there is a connection error), it prints a 
message saying the site is down along with the elapsed time.

You can modify this code to add additional functionality, such as checking the site at 
regular intervals or storing the response times in a database for later analysis.'''