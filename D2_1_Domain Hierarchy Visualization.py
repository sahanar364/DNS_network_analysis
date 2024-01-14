#Domain Hierarchy Visualization

import scapy.all as scapy
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

# Read the pcap file containing DNS traffic
pcap_file = "capture.pcap"
pcap = scapy.rdpcap(pcap_file)

# Create a directed graph to represent domain hierarchy
domain_hierarchy = nx.DiGraph()

# Extract DNS query names and build the hierarchy
for packet in pcap:
    if packet.haslayer(scapy.DNSQR):
        query_name = packet[scapy.DNSQR].qname.decode()
        domain_parts = query_name.split('.')
        for i in range(len(domain_parts) - 1):
            parent_domain = ".".join(domain_parts[i:])
            child_domain = ".".join(domain_parts[i + 1:])
            domain_hierarchy.add_edge(parent_domain, child_domain)

# Customize the graph visualization
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(domain_hierarchy, seed=42)  # Seed for reproducibility
node_sizes = [3000 if node == '' else 1000 for node in domain_hierarchy.nodes()]  # Larger root node

# Draw the nodes and edges with labels
nx.draw_networkx_nodes(domain_hierarchy, pos, node_size=node_sizes, node_color='lightblue', alpha=0.9)
nx.draw_networkx_edges(domain_hierarchy, pos, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(domain_hierarchy, pos, font_size=8)

# Add title and axis labels
plt.title("Domain Hierarchy Visualization")
plt.xlabel("Parent Domains")
plt.ylabel("Child Domains")

# Show the plot
plt.axis('off')  # Turn off axis labels
plt.tight_layout()
plt.show()
