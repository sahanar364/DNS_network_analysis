#Query vs. Response Latency

import matplotlib.pyplot as plt
from scapy.all import IP, TCP, send
import time

# Create lists to store latency data for queries and responses
query_latencies = []
response_latencies = []

# Function to send a query packet and measure latency
def send_query(destination_ip, destination_port, is_abnormal=False):
    start_time = time.time()
    query_packet = IP(dst=destination_ip) / TCP(dport=destination_port)
    response_packet = send(query_packet, verbose=False, return_packets=True)[0]
    end_time = time.time()
    latency = (end_time - start_time) * 1000  # Convert to milliseconds
    query_latencies.append(latency)
    response_latencies.append(0)  # Placeholder for response latency

    if is_abnormal:
        # Introduce spikes for abnormal traffic by adding a fixed value to latency
        query_latencies[-1] += 50

# Function to send a response packet and measure latency
def send_response(destination_ip, source_port, is_abnormal=False):
    start_time = time.time()
    response_packet = IP(dst=destination_ip) / TCP(sport=source_port)
    send(response_packet, verbose=False)
    end_time = time.time()
    latency = (end_time - start_time) * 1000  # Convert to milliseconds
    response_latencies[-1] = latency  # Update the last entry with response latency

    if is_abnormal:
        # Introduce spikes for abnormal traffic by adding a fixed value to latency
        response_latencies[-1] += 50

# Send a series of query-response packets and measure latencies, introducing spikes for abnormal traffic
for _ in range(10):
    send_query("192.168.1.2", 80, is_abnormal=(_ >= 3 and _ <= 7))  # Define abnormal traffic
    send_response("192.168.1.2", 80, is_abnormal=(_ >= 3 and _ <= 7))  # Define abnormal traffic

# Create a scatter plot for query and response latencies
plt.figure(figsize=(10, 6))
query_x = list(range(1, len(query_latencies) + 1))
plt.scatter(query_x, query_latencies, label='Query Latency', marker='o')
plt.scatter(query_x, response_latencies, label='Response Latency', marker='x')

# Highlight abnormal traffic in red
abnormal_x = [x for x in query_x if 3 <= x <= 7]
abnormal_query_latencies = [query_latencies[x - 1] for x in abnormal_x]
abnormal_response_latencies = [response_latencies[x - 1] for x in abnormal_x]
plt.scatter(abnormal_x, abnormal_query_latencies, c='red', label='Abnormal Query Latency', marker='o')
plt.scatter(abnormal_x, abnormal_response_latencies, c='red', label='Abnormal Response Latency', marker='x')

plt.xlabel('Packet Number')
plt.ylabel('Latency (ms)')
plt.title('Query vs. Response Latency')
plt.legend()
plt.grid(True)
plt.show()




