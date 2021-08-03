# Verificar se site está acessível ou não
import urllib.request


def status_site(url):
    try:
        status = urllib.request.urlopen(url).getcode()
    except urllib.error.URLError:
        status = 0
    return status


site = 'http://www.pudim.com.br/'
if status_site(site) == 200:
    print(f'\u001b[36mSite acessível.')
else:
    print(f'\u001b[31mSite indisponível.')

site = 'http://www.pudim2.com.br/'
if status_site(site) == 200:
    print(f'\u001b[36mSite acessível.')
else:
    print(f'\u001b[31mSite indisponível.')