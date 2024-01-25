import scapy.all as scapy
# Crea un objeto de interfaz de red
interface = scapy.get_if_list()[0]
# Inicializa el sniffer de paquetes
sniffer = scapy.sniff(iface=interface, store=False)
# Captura los paquetes de datos
for packet in sniffer:
    # Analiza los paquetes de datos
    print(packet.summary())