#Ex 62: Melhore o desafio 61 pergutnando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

'''primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
escolha = ''
n = 0
termos = 11

while cont <= termos:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
    if cont == 10:
        n = int(input('Quantos termos você quer mostrar a mais? '))
        termos += n
        while cont <= termos:
            print(f'{termo} -> ', end='')
            termo += razao
            cont += 1'''


primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim')