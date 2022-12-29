
import sys

# sys is a package
#numpy
print("User Current Version:-", sys.version)

import socket
hostname = socket.gethostname()
print(hostname)
ipadd = socket.gethostbyname(hostname)
print(ipadd)
