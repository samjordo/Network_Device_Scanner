import netifaces
import ipaddress
import ctypes
from scapy.all import arping
import nmap

#use netifaces to get the ip address and mask of the interface and then use ipaddress to get the range of the network
addr = netifaces.ifaddresses('MediaTek Wi-Fi 6 MT7921 Wireless LAN Card')[netifaces.AF_INET][0]['addr']
mask = netifaces.ifaddresses('MediaTek Wi-Fi 6 MT7921 Wireless LAN Card')[netifaces.AF_INET][0]['mask']
range = ipaddress.ip_interface(f"{addr}/{mask}").network

#check priveleges for scapy
if not (ctypes.windll.shell32.IsUserAnAdmin()):
    print("You need to run this script as an administrator")
    exit(1)

#send an ARP request to the range of the network and get the MAC addresses of the devices on the network
answered, unanswered = arping(str(range))
targets = [received.psrc for sent, received in answered]
for target in targets:
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sS -T4 -p 1-65535')
    print(nm[target]['tcp'].keys())


