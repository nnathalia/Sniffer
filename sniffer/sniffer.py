from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

def process_packet(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OUTRO"
        port_src = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else "N/A"
        port_dst = packet[TCP].dport if TCP in packet else packet[UDP].dport if UDP in packet else "N/A"
        payload = packet[Raw].load if Raw in packet else b"(sem payload)"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] {proto} | {ip_src}:{port_src} → {ip_dst}:{port_dst}")
        print(f"Payload: {payload[:100]}\n{'-'*60}")

# Captura apenas pacotes TCP e UDP
print("Sniffer iniciado... (CTRL+C para sair)")
sniff(filter="tcp or udp", prn=process_packet, store=0)
