import requests
def site(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


teste = 'https://www.pudim.com.br'
if site(teste):
    print('Pudim esta acessivel')
else:
    print('Pudim nao esta acessivel')

