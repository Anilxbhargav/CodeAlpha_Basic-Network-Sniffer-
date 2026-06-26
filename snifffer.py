from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"""
Source IP: {packet[IP].src}
Destination IP: {packet[IP].dst}
Protocol: {packet[IP].proto}
-----------------------------
""")

print("Starting Network Sniffer...")
sniff(prn=packet_callback, count=10)