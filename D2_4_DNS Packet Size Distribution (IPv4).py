#DNS Packet Size Distribution (IPv4)

import matplotlib.pyplot as plt
import random

# Define the number of DNS packets and their sizes
num_packets = 100
packet_sizes = [random.randint(40, 150) for _ in range(num_packets)]

# Introduce spikes for abnormal packet sizes
abnormal_packets = [random.randint(80, 120) for _ in range(10)]
for i in range(10):
    packet_sizes[random.randint(0, num_packets - 1)] = abnormal_packets[i]

# Create a histogram for DNS Packet Size Distribution
plt.figure(figsize=(10, 6))
plt.hist(packet_sizes, bins=15, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Frequency')
plt.title('DNS Packet Size Distribution (IPv4)')
plt.grid(True)

# Highlight abnormal packet sizes in red
for size in abnormal_packets:
    plt.axvline(x=size, color='red', linestyle='--', label='Abnormal Size')

plt.legend()
plt.show()
