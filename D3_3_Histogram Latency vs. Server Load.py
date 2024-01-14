#Histogram: Latency vs. Server Load

import matplotlib.pyplot as plt
import random

# Define the number of data points
num_data_points = 10

# Create lists to store latency and server load data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
server_load = [random.uniform(0, 80) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    server_load[interval - 1] += 30

# Create a histogram for Latency vs. Server Load
plt.figure(figsize=(10, 6))
plt.hist(latency, bins=10, alpha=0.5, label='Latency (ms)', color='blue')
plt.hist(server_load, bins=10, alpha=0.5, label='Server Load (%)', color='green')

# Highlight abnormal data points in red
for i in abnormal_intervals:
    plt.axvline(x=latency[i - 1], color='red', linestyle='dashed', label='Abnormal Latency' if i == abnormal_intervals[0] else '')
    plt.axvline(x=server_load[i - 1], color='red', linestyle='dashed', label='Abnormal Server Load' if i == abnormal_intervals[0] else '')

plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram: Latency vs. Server Load')
plt.legend()
plt.grid(True)
plt.show()
