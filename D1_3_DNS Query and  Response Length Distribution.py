#DNS Query and  Response Length Distribution

import scapy.all as scapy
import matplotlib.pyplot as plt

pcap = scapy.rdpcap("capture.pcap")

dns_queries = [packet[scapy.DNSQR] for packet in pcap if packet.haslayer(scapy.DNSQR)]
dns_responses = [packet[scapy.DNSRR] for packet in pcap if packet.haslayer(scapy.DNSRR)]

query_lengths = [len(query) for query in dns_queries]
response_lengths = [len(response) for response in dns_responses]

# Define a threshold for abnormal query and response lengths (e.g., 100 bytes)
abnormal_threshold = 100

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
# Highlight abnormal query lengths in red
abnormal_query_lengths = [qlen for qlen in query_lengths if qlen > abnormal_threshold]
plt.hist(query_lengths, bins=20, color='b', alpha=0.7, label='Normal')
plt.hist(abnormal_query_lengths, bins=20, color='r', alpha=0.7, label='Abnormal')
plt.xlabel("Query Length (bytes)")
plt.ylabel("Number of Queries")
plt.title("DNS Query Length Distribution")
plt.legend()

plt.subplot(2, 1, 2)
# Highlight abnormal response lengths in red
abnormal_response_lengths = [rlen for rlen in response_lengths if rlen > abnormal_threshold]
plt.hist(response_lengths, bins=20, color='g', alpha=0.7, label='Normal')
plt.hist(abnormal_response_lengths, bins=20, color='r', alpha=0.7, label='Abnormal')
plt.xlabel("Response Length (bytes)")
plt.ylabel("Number of Responses")
plt.title("DNS Response Length Distribution")
plt.legend()

plt.tight_layout()
plt.show()

