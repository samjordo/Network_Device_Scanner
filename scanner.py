import netifaces
import ipaddress
import os
from scapy.all import *

#use netifaces to get the ip address and mask of the interface and then use ipaddress to get the range of the network
addr = netifaces.ifaddresses('MediaTek Wi-Fi 6 MT7921 Wireless LAN Card')[netifaces.AF_INET][0]['addr']
mask = netifaces.ifaddresses('MediaTek Wi-Fi 6 MT7921 Wireless LAN Card')[netifaces.AF_INET][0]['mask']
range = ipaddress.ip_interface(f"{addr}/{mask}").network

#check priveleges for scapy
if not (os.geteuid() == 0):
    print("You need to run this script as root")
    exit(1)

#send an ARP request to the range of the network and get the MAC addresses of the devices on the network
result = arping(str(range), verbose=False)

