import scapy.all as scapy
from scapy.all import *
"""ip = IP()
print(ip)
print(ip.show())
my_frame = Ether() / IP() # /ARP() / ICMP()
print(my_frame)
print(my_frame.show())
"""

s = IP(dst="google.com")/ICMP()
print(s.show())