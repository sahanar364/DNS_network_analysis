#Latency vs. Response Rate (req/sec)

import matplotlib.pyplot as plt
import random
import numpy as np

# Define the number of data points
num_data_points = 10

# Create lists to store latency and response rate data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
response_rate = [random.uniform(100, 500) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    response_rate[interval - 1] -= 50

# Create a bar graph for Latency vs. Response Rate
plt.figure(figsize=(10, 6))
x = np.arange(num_data_points)
width = 0.35
plt.bar(x - width/2, latency, width, label='Latency (ms)', color='blue', alpha=0.7)
plt.bar(x + width/2, response_rate, width, label='Response Rate (req/sec)', color='green', alpha=0.7)

# Highlight abnormal data points in red
abnormal_indices = [i for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.bar(abnormal_indices, [latency[i] for i in abnormal_indices], width, color='red', label='Abnormal Latency')
plt.bar(abnormal_indices, [response_rate[i] for i in abnormal_indices], width, color='red', label='Abnormal Response Rate')

plt.xlabel('Data Point')
plt.ylabel('Latency (ms) / Response Rate (req/sec)')
plt.title('Latency vs. Response Rate (req/sec)')
plt.xticks(x, range(1, num_data_points + 1))
plt.legend()
plt.grid(True)
plt.show()
