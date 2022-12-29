import scapy.all as scapy
from scapy.all import *
my_frame = Ether() / IP()
print(my_frame)
print(my_frame.show())