'''This code defines a function compute that simulates a long-running computation by sleeping for 1 second. 
It then creates a thread for each computation and starts the threads. Finally, it waits for the threads to 
complete using the join method.

When run, this code will start 5 threads, each of which will perform a long-running computation. The main 
thread will then wait for all of the threads to complete before printing "All computations completed" to 
the console.

This is a simple example of using threads in Python, but it should give you an idea of how to create and 
manage threads in your own programs.'''

import threading
import time

def compute(n):
    # Simulate a long-running computation
    print(f"Starting computation for {n}")
    time.sleep(1.0)
    print(f"Finished computation for {n}")

# Create a thread for each computation
threads = [threading.Thread(target=compute, args=(n,)) for n in range(5)]

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to complete
for thread in threads:
    thread.join()

print("All computations completed")
