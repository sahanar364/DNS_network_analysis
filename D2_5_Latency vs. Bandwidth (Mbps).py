#Latency vs. Bandwidth (Mbps)

import matplotlib.pyplot as plt
import random
import numpy as np

# Define the number of data points
num_data_points = 10

# Create lists to store latency and bandwidth data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
bandwidth = [random.uniform(10, 100) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    bandwidth[interval - 1] -= 20

# Create a bar graph for Latency vs. Bandwidth
plt.figure(figsize=(10, 6))
x = np.arange(num_data_points)
width = 0.35
plt.bar(x - width/2, latency, width, label='Latency (ms)', color='blue', alpha=0.7)
plt.bar(x + width/2, bandwidth, width, label='Bandwidth (Mbps)', color='green', alpha=0.7)

# Highlight abnormal data points in red
abnormal_indices = [i for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.bar(abnormal_indices, [latency[i] for i in abnormal_indices], width, color='red', label='Abnormal Latency')
plt.bar(abnormal_indices, [bandwidth[i] for i in abnormal_indices], width, color='red', label='Abnormal Bandwidth')

plt.xlabel('Data Point')
plt.ylabel('Latency (ms) / Bandwidth (Mbps)')
plt.title('Latency vs. Bandwidth (Mbps)')
plt.xticks(x, range(1, num_data_points + 1))
plt.legend()
plt.grid(True)
plt.show()
