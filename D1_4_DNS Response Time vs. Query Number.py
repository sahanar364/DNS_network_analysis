#DNS Response Time vs. Query Number

import matplotlib.pyplot as plt
import dns.resolver
import time

# Create lists to store query numbers and DNS response times
query_numbers = []
dns_response_times = []

# Function to query a DNS server and measure response time
def query_dns(domain_name, dns_server, query_number, is_abnormal=False):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]

    start_time = time.time()
    try:
        response = resolver.query(domain_name)
    except dns.exception.DNSException:
        response = None
    end_time = time.time()

    if response:
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        if is_abnormal:
            latency += 50  # Introduce spikes for abnormal traffic
        query_numbers.append(query_number)
        dns_response_times.append(latency)
    else:
        query_numbers.append(query_number)
        dns_response_times.append(0)  # Placeholder for failed queries

# Query the DNS server and measure response times, introducing spikes for abnormal traffic
for query_number in range(1, 11):
    is_abnormal = (query_number >= 3 and query_number <= 7)
    query_dns("example.com", "8.8.8.8", query_number, is_abnormal=is_abnormal)

# Create a plot for DNS response times as "Response Time vs. Query Number"
plt.figure(figsize=(10, 6))
plt.plot(query_numbers, dns_response_times, marker='o', linestyle='-')

# Highlight abnormal periods in red
abnormal_query_numbers = [query_numbers[i] for i in range(len(query_numbers)) if dns_response_times[i] > 0 and 3 <= query_numbers[i] <= 7]
abnormal_response_times = [dns_response_times[i] for i in range(len(query_numbers)) if dns_response_times[i] > 0 and 3 <= query_numbers[i] <= 7]
plt.scatter(abnormal_query_numbers, abnormal_response_times, c='red', label='Abnormal Response Times', marker='o')

plt.xlabel('Query Number')
plt.ylabel('Response Time (ms)')
plt.title('DNS Response Time vs. Query Number')
plt.grid(True)
plt.show()



