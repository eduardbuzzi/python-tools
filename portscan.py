# Python 2.7

import socket
import os
ip = raw_input("Informe o IP => ")
ports = range(65535)

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.6)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) + " => Porta Aberta"
print "Scan Finalizado."
