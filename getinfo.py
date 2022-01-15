import netmiko
from netmiko import ConnectHandler

SWITCH= {'device_type':'cisco_ios', 'ip':'10.211.10.36', 'username':'samer',
'password':'cisco','secret':'cisco'}

net_connect=ConnectHandler(**SWITCH)
#net_connect.enable()
start_output=net_connect.send_command('show version')
display_it=(start_output.index('Version'))
print (display_it)
print (start_output[display_it:(display_it+60)])





