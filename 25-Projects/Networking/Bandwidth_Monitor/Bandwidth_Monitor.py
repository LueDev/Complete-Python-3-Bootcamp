'''This code uses the net_io_counters function from the psutil library 
to get the network statistics for each network interface. It then prints 
the statistics for each interface, including the number of bytes sent and received.

This is a very simple example of a bandwidth monitor in Python, but it should give 
you an idea of how to use the psutil library to monitor the bandwidth usage of your 
system. You can customize the monitor by filtering the interfaces, collecting 
statistics over a period of time, and performing other tasks as needed.'''

import psutil

def bandwidth_monitor():
    # Get the network statistics
    net_stats = psutil.net_io_counters(pernic=True)

    # Print the statistics for each network interface
    for interface, stats in net_stats.items():
        print(f"Interface: {interface}")
        print(f"Bytes sent: {stats.bytes_sent}")
        print(f"Bytes received: {stats.bytes_recv}")
        print()

bandwidth_monitor()
