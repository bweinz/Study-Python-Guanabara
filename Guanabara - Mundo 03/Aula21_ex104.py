#Crie um programa que tenha a função leiaInt() que vai funcionar de fomra semelhante a função input() do python.
#Só que fazendo a validação para aceitar apenas um valor númerio
#Ex: n = leiaInt('Digite um n')


def leiaInt(msg):
    ok = False                          #Ok começa como Falso
    valor = 0
    while True:
        n = str(input(msg))             #n recebe uma string
        if n.isnumeric():               # se n for um numero
            valor = int(n)              #transoforme o valor em int
            ok = True                   #ok recebe True
        else:
            print('\033[0;31mErro, Digite um numero inteiro Valido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')