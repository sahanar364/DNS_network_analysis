#Query Rate vs. Response Rate over Time

import matplotlib.pyplot as plt
import random

# Create time intervals and initialize query and response rates
time_intervals = list(range(1, 11))
query_rate = [random.randint(10, 30) for _ in time_intervals]
response_rate = [random.randint(10, 30) for _ in time_intervals]

# Introduce spikes for abnormal query and response rates
abnormal_intervals = [3, 6, 9]
for interval in abnormal_intervals:
    query_rate[interval - 1] += 20
    response_rate[interval - 1] -= 20

# Create a plot for Query Rate vs. Time
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, query_rate, label='Query Rate', marker='o', linestyle='-')

# Highlight abnormal query rates in red
abnormal_query_rate = [query_rate[i] for i in range(len(time_intervals)) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_query_rate, c='red', label='Abnormal Query Rate', marker='o')

# Create a plot for Response Rate vs. Time
plt.plot(time_intervals, response_rate, label='Response Rate', marker='x', linestyle='-')

# Highlight abnormal response rates in red
abnormal_response_rate = [response_rate[i] for i in range(len(time_intervals)) if i + 1 in abnormal_intervals]
plt.scatter(abnormal_intervals, abnormal_response_rate, c='red', label='Abnormal Response Rate', marker='x')

plt.xlabel('Time Intervals')
plt.ylabel('Rate')
plt.title('Query Rate vs. Response Rate over Time')
plt.legend()
plt.grid(True)
plt.show()

