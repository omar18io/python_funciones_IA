import scapy.all as scapy
from scapy.layers import http
def sniif(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)
def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print("*",100)
        print(packet.show())
        print("*",100)
def main():
    sniif("Wi-Fi")
if __name__ == "__main__":
    main()