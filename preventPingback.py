# Must run as administrator
import subprocess

hosts = open("C:/Windows/system32/drivers/etc/hosts", "r")
content = hosts.read()
hosts.close()
commented = "#192.168.1.45" in content # 192.168.1.45 is my local server IP

if "SSID" in str(subprocess.check_output("netsh wlan show interfaces")): # Change SSID for your local network SSID (in which the server is located)
    if commented:
        hostsFile = open("C:/Windows/system32/drivers/etc/hosts", "w")
        hostsFile.write(content.replace("#192.168.1.45", "192.168.1.45"))
        hostsFile.close()
else:
    if not commented:
        hostsFile = open("C:/Windows/system32/drivers/etc/hosts", "w")
        hostsFile.write(content.replace("192.168.1.45", "#192.168.1.45"))
        hostsFile.close()
