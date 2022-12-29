from netmiko import ConnectHandler

"""
Router={
	"device_type": "cisco_ios",
	"ip": "sandbox-iosxe-latest-1.cisco.com",
	"username": "developer",
	"password": "C1sco12345"
}
"""

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**Router)

        print('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)

net_connect.disconnect()
from netmiko import ConnectHandler
CSR={
	"device_type": "cisco_ios",
	"ip": "sandbox-iosxe-latest-1.cisco.com",
	"username": "developer",
	"password": "C1sco12345"
}
net_connect = ConnectHandler(**CSR)
hostname=net_connect.send_command('show run | i host')
hostname.split(" ")
hostname, device,*rest=hostname.split(" ")
print("Backing up" + device)
filename="C:/Users/user716/PycharmProjects/pythonProject1/devices.txt"
showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()