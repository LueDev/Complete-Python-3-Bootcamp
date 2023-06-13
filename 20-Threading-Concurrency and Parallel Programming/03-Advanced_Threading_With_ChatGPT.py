import threading
import time

class ComputeThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None
    
    def run(self):
        # Simulate a long-running computation
        print(f"\nStarting computation for {self.n}")
        time.sleep(1.0)
        print(f"\nFinished computation for {self.n}")
        self.result = self.n ** 2

# Create a thread for each computation
threads = [ComputeThread(n) for n in range(5)]

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to complete
for thread in threads:
    thread.join()

# Print the results
for thread in threads:
    print(f"Result for {thread.n}: {thread.result}")
