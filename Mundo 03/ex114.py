import urllib.request
import urllib.error

def verificar_site(url):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36'}
        req = urllib.request.Request(url, headers=header)
        site = urllib.request.urlopen(req, timeout=10)

        return f'\033[32mConsegui acessar o site "{url}" com sucesso\033[m'
    except urllib.error.URLError:
        return f'\033[31mO site "{url}" não está acessível no momento.\033[m'


print(verificar_site('http://www.pudim.com.br'))
