#Faça um mini sistema que utilize o interactive help do python. o Usuario vai digitar o comando e o manual vaia parecer
#Quando o usuário digitar a palavra fim o programa se encerrará.


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


#Programa Principal
comando = ''
while True:
    titulo('Sistema de Ajuda Pyhelp')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo')