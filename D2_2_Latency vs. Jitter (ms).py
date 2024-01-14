#Latency vs. Jitter (ms)

import matplotlib.pyplot as plt
import random

# Define the number of data points
num_data_points = 10

# Create lists to store latency and jitter data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
jitter = [random.uniform(1, 5) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    jitter[interval - 1] += 2

# Create a plot for Latency vs. Jitter
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_data_points + 1), latency, label='Latency (ms)', marker='o', linestyle='-')
abnormal_latency = [latency[i] for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_latency, c='red', label='Abnormal Latency', marker='o')
plt.plot(range(1, num_data_points + 1), jitter, label='Jitter (ms)', marker='^', linestyle='-')
abnormal_jitter = [jitter[i] for i in range(num_data_points) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_jitter, c='red', label='Abnormal Jitter', marker='^')
plt.xlabel('Data Point')
plt.ylabel('Latency (ms) / Jitter (ms)')
plt.title('Latency vs. Jitter (ms)')
plt.legend()
plt.grid(True)
plt.show()


