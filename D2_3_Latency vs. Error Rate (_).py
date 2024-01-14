#Latency vs. Error Rate (%)

import matplotlib.pyplot as plt
import random

# Define the number of data points
num_data_points = 10

# Create lists to store latency and error rate data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
error_rate = [random.uniform(0, 3) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    error_rate[interval - 1] += 1

# Create a plot for Latency vs. Error Rate
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_data_points + 1), latency, label='Latency (ms)', marker='o', linestyle='-')
abnormal_latency = [latency[i] for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_latency, c='red', label='Abnormal Latency', marker='o')
plt.plot(range(1, num_data_points + 1), error_rate, label='Error Rate (%)', marker='x', linestyle='-')
abnormal_error_rate = [error_rate[i] for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_error_rate, c='red', label='Abnormal Error Rate', marker='x')
plt.xlabel('Data Point')
plt.ylabel('Latency (ms) / Error Rate (%)')
plt.title('Latency vs. Error Rate (%)')
plt.legend()
plt.grid(True)
plt.show()
