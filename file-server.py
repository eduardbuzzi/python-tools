import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = int(raw_input("Informe a Porta que vai ser usada para escutar => "))
nome = str(raw_input("Nome do Arquivo que vai ser salvo => "))

file = open(nome, 'w')

try:
    server.bind((ip, port))
    server.listen(5)
    print "Escutando em " + ip + ":" + str(port)
    (client_socket, address) = server.accept()
    print "Recebendo de " + address[0]
    data = client_socket.recv(1024)
    file.write(data)
    server.close()
except Exception as erro:
    print "Erro: " + str(erro)
