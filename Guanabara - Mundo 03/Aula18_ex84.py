#Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final Mostre:
'''
a) Quantas pessoas foram cadastradas:
B) Uma listagem com as pessoas mais pesadas:
C) uma listagem com as pessoas mais leves:
'''

'''temporario = []
principal = []
maior = menor = 0
contador = 0

while True:

    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))

    if contador == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    r = str(input('Continuar S/N? '))
    principal.append(temporario[:])
    temporario.clear()
    contador += 1
    if r in 'Nn':
        break


print(f'O mais pesado pesa: {maior} e o mais leve {menor}', end='')

for p in principal:
    if principal[1] == maior:
        print(f'{principal[0]}', end='')

for p in principal:
    if principal[1] == menor:
        print(f'{principal[0]}', end='')'''


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continuar? S/N'))
    if resp in 'Nn':
        break

print('-=' *30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg, Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg, Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

