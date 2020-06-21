# Python 2.7

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

ip = str(raw_input("Informe o IP para se conectar => "))
port = int(raw_input("Informe a Porta para se conectar => "))

try:
    client.connect((ip, port))
    data = raw_input("Enviar => ")
    client.send(data)
    pacotes = client.recv(1024)
    print pacotes
except:
    print "Conexao falhou!"
