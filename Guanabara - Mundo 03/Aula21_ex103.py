#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente;


def ficha(a='Desconhecido', b = 0):
    if a == '':
        a = '<Desconhecido>'
    if b == '':
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato')


a = input('Nome do Jogador: ')
b = input('Número de Gols: ')
ficha(a, b)

'''#Solução Guanabara:

def ficha(jog= '<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


#Programa principal
nome= str(input("Nome do Jogador: "))
gols = str(input("Numero de gols: "))
if gols.isnumeric():                            #Gols é numerico?
    gols = int(gols)                            #Se for então Gols vira int
else:                                           #Senão
    gols = 0                                    #Gols vale 0
if nome.strip() == '':                          #Se o nome sem nenhum espaço ficou vazil
    ficha(gol=gols)                                #Se estiver sem nome vazil, chamo somente a ficha com valor de gol
else:
    ficha(nome,gols)                                  #Se não estiver vazio chamo a ficha com o valor de nome e de gol'''