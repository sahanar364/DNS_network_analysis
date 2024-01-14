#Stacked Bar Chart: Latency vs. Location

import matplotlib.pyplot as plt
import random

# Define the number of data points
num_data_points = 5

# Define locations and create lists to store latency data
locations = ['Location A', 'Location B', 'Location C', 'Location D', 'Location E']
latency = []

for _ in range(num_data_points):
    latency.append([random.uniform(5, 20) for _ in range(len(locations))])

# Introduce spikes for abnormal behavior
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    if interval <= num_data_points:
        for i in range(len(locations)):
            latency[interval - 1][i] += 10

# Create a stacked bar chart for Latency vs. Location
plt.figure(figsize=(10, 6))

x = range(1, num_data_points + 1)
bottom = [0] * len(locations)

for i in range(len(locations)):
    plt.bar(x, [latency[j][i] for j in range(num_data_points)], label=locations[i], bottom=bottom)
    bottom = [latency[j][i] + bottom[j] for j in range(num_data_points)]

# Highlight abnormal data points in red and label them
for i in abnormal_intervals:
    if i <= num_data_points:
        for j in range(len(locations)):
            plt.bar(i, latency[i - 1][j], color='red')
            plt.text(i, bottom[j], f'Abnormal\n({i})', ha='center', va='bottom', color='red')

plt.xlabel('Data Point')
plt.ylabel('Latency (ms)')
plt.title('Stacked Bar Chart: Latency vs. Location')
plt.legend()
plt.grid(True)
plt.show()

