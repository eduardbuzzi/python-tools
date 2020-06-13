import socket
from time import ctime

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

user = raw_input("Informe seu nome => ")
amigo = raw_input("Informe o nome com quem vai conversar => ")
ipamigo = raw_input("Informe o IP do(a) " + amigo + " => ")
portamigo = raw_input("Informe a Porta que " + amigo + " abriu para se comunicar => ")

try:
    while True:
        print
        uservar = raw_input(user + " => ")
        client.sendto(uservar, (ipamigo, int(portamigo)))
        client.settimeout(900)
        msg, friend = client.recvfrom(1024)
        time = ctime().split()[3]
        print time + " - " + amigo + " (" + friend[0] + ") => " + msg
    client.close()

except Exception as erro:
    print "Conexao Falhou!"
    print erro
    client.close()
