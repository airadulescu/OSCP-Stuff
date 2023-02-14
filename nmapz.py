# This script is to take in a list of IPs from IP.txt and scan each open port for each live IP

import os
import nmap

nm = nmap.PortScanner()

IP = open('IP.txt','r')
lst = {}

i = 0

for l in IP:
  lst[l.strip('\n')] = []

while i < len(lst):
  ip = list(lst.keys())[i]
  print(f'Scanning {ip} Ports 0 to 65535')
  nm.scan(list(lst.keys())[i],'0-65535')
  lst[list(lst.keys())[i]] = list(nm[list(lst.keys())[i]]['tcp'].keys())[:]
  print(f'Added Ports {lst[list(lst.keys())[i]]}')
  ports = ','.join([str(x) for x in lst[list(lst.keys())[i]]])
  print(f'Full Port Scan: {ip} on ports {ports}')
  os.system(f'nmap -sC -sV {ip} -p {ports} -oN nmap/{ip}.txt -vvv')
  i += 1
