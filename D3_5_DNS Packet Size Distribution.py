#DNS Packet Size Distribution

import scapy.all as scapy
import matplotlib.pyplot as plt

# Read the pcap file containing DNS traffic
pcap_file = "capture.pcap"
pcap = scapy.rdpcap(pcap_file)

# Define a threshold for abnormal packet sizes (adjust as needed)
abnormal_size_threshold = 100  # For example, consider sizes above 100 bytes as abnormal

# Create lists to store DNS packet sizes
normal_sizes = []
abnormal_sizes = []

# Extract DNS packet sizes and classify them
for packet in pcap:
    if packet.haslayer(scapy.DNS):
        packet_size = len(packet)
        if packet_size > abnormal_size_threshold:
            abnormal_sizes.append(packet_size)
        else:
            normal_sizes.append(packet_size)

# Plot DNS packet size distribution
plt.figure(figsize=(10, 6))

# Use 'alpha' to make overlapping bars visible
plt.hist(normal_sizes, bins=20, alpha=0.7, label="Normal Packets", color='b')
plt.hist(abnormal_sizes, bins=20, alpha=0.7, label="Abnormal Packets", color='r')

plt.xlabel("Packet Size (Bytes)")
plt.ylabel("Number of Packets")
plt.title("DNS Packet Size Distribution (IPv4)")
plt.grid(True)
plt.legend()
plt.show()

