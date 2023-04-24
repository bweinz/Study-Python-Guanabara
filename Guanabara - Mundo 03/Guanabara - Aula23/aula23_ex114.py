#Crie um código em Python que teste se o site Pudim está acessivel pelo computador do usuario.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site pudim com sucesso')
    print(site.read())    #aparece o codigo HTML inteiro da pagina