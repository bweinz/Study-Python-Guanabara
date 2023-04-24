#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até Logo!')
        break
    else:
        cabeçalho('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

