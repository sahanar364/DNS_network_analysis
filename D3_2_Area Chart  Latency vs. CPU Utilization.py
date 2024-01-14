#Area Chart: Latency vs. CPU Utilization

import matplotlib.pyplot as plt
import random

# Define the number of data points
num_data_points = 10

# Create lists to store latency and CPU utilization data
latency = [random.uniform(5, 20) for _ in range(num_data_points)]
cpu_utilization = [random.uniform(0, 100) for _ in range(num_data_points)]

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    latency[interval - 1] += 10
    cpu_utilization[interval - 1] += 20

# Create an area chart for Latency vs. CPU Utilization
plt.figure(figsize=(10, 6))
x = range(1, num_data_points + 1)
plt.fill_between(x, latency, label='Latency (ms)', color='blue', alpha=0.5)
plt.fill_between(x, cpu_utilization, label='CPU Utilization (%)', color='green', alpha=0.5)

# Highlight abnormal data points in red
for i in abnormal_intervals:
    plt.scatter(i, latency[i - 1], c='red', marker='o')
    plt.scatter(i, cpu_utilization[i - 1], c='red', marker='o')

plt.xlabel('Data Point')
plt.ylabel('Values')
plt.title('Area Chart: Latency vs. CPU Utilization')
plt.legend()
plt.grid(True)
plt.show()
