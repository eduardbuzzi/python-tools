import paramiko

host = raw_input("Informe o IP => ")
user = raw_input("Informe o User => ")
passwd = raw_input("Informe a Password de " + user + " => ")

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(host, username=user, password=passwd)

    while True:
        comando = raw_input("Comando: ")
        entrada, saida, erros = client.exec_command(comando)
        print saida.readlines()

except Exception:
    print "Falha de Autenticacao!"
