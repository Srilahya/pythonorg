import scapy.all as scapy
from scapy.all import *

a=IP(ttl=10)
print(a)
print(a.src)