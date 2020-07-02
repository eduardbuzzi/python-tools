import urllib2
import urllib

url = 'http://www.burgerking.com.br/'
cabecalho = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
}

try:

    requisicao = urllib2.Request(url, headers=cabecalho)
    resposta = urllib2.urlopen(requisicao)
    html = resposta.read()
    print html
except Exception as erro:
    print erro
