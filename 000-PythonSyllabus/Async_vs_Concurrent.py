'''Concurrency and asynchronous programming are related concepts that are often used to improve 
the performance and scalability of applications. Here is a brief overview of the differences between the two:

Concurrency refers to the ability of a system or application to perform multiple tasks concurrently, or at 
the same time. Concurrency allows a system to make better use of its resources by allowing multiple tasks 
to run in parallel, rather than sequentially.

Asynchronous programming refers to a programming paradigm in which the flow of control is not tied to the 
order of execution of code. In asynchronous programming, a task is launched and the program continues to 
execute, rather than waiting for the task to complete. This allows the program to perform other tasks in 
the meantime, improving performance and responsiveness.

Both concurrency and asynchronous programming can be used to improve the performance and scalability of 
applications, but they are not the same thing. Concurrency refers to the ability to perform multiple tasks 
at the same time, while asynchronous programming refers to a programming paradigm that allows tasks to be 
executed out of order.'''

import asyncio
import concurrent.futures

async def compute_async(x, y):
    # Asynchronously compute the sum of x and y
    print(f"Compute {x} + {y}")
    await asyncio.sleep(1.0)
    return x + y

def compute_concurrent(x, y):
    # Concurrently compute the product of x and y
    print(f"Compute {x} * {y}")
    return x * y

async def main():
    # Use a concurrent.futures.ThreadPoolExecutor to execute compute_concurrent concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, compute_concurrent, x, y)
            for x, y in [(2, 3), (3, 4), (4, 5)]
        ]
        # Wait for the concurrent tasks to complete
        results = await asyncio.gather(*futures)
        print(results)

    # Use asyncio.create_task to execute compute_async asynchronously
    tasks = [compute_async(x, y) for x, y in [(2, 3), (3, 4), (4, 5)]]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
