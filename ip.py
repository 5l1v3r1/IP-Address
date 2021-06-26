import requests
from subprocess import check_output
from  tabulate import tabulate

def Public_IP():
	public_ip = requests.get('https://api.ipify.org/?format=raw').content.decode()
	return public_ip



def Private():
	data = check_output(['ip', 'addr', 'show', 'wlan0']).decode().split('\n')
	for each in data:
		if 'inet ' in each:
			data = each.split('/')[0].strip().split(' ')[1]
	return data


try:
	ips = [['Public IP', 'Private IP'], [Public_IP(), Private()]]
except:
	ips = [['Public IP'], [Public_IP()]]

print(tabulate(ips, headers="firstrow", tablefmt="grid"))


# Made by CyberTitus
# Credits: https://api.ipify.org/