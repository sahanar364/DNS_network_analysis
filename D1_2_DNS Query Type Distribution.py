#DNS Query Type Distribution

# Import necessary libraries
import scapy.all as scapy
import matplotlib.pyplot as plt

# Read the pcap file
pcap = scapy.rdpcap("capture.pcap")

# Extract DNS queries from the pcap file
dns_queries = [packet[scapy.DNSQR] for packet in pcap if packet.haslayer(scapy.DNSQR)]

# Initialize a dictionary to store query type counts
query_types = {}

# Count the occurrences of each DNS query type
for query in dns_queries:
    qtype = query.qtype
    query_types[qtype] = query_types.get(qtype, 0) + 1

# Prepare data for the pie chart
labels = ['IPv6 Reverse DNS (PTR)', 'IPv4 DNS (A)', 'IPv4 Reverse DNS (PTR)']  # Labels for DNS query types
sizes = [query_types.get(65, 0), query_types.get(1, 0), query_types.get(12, 0)]  # Counts of each query type

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)  # Pie chart with labels and percentages
plt.title("DNS Query Type Distribution")  # Set the title

# Ensure an equal aspect ratio for a circular pie chart
plt.axis('equal')

# Show the pie chart
plt.show()

