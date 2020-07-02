import requests

url = 'http://www.burgerking.com.br'

cabecalho = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
}

resposta = requests.get(url, headers=cabecalho)
