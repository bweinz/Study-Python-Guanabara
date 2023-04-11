#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso, crie 2 listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente.
#Ao final mostre o conteudo das três listas Geradas


'''lista = []
plista = []
ilista = []


while True:

    valor = int(input('Digite um Valor: '))
    lista.append(valor)
    r = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if valor % 2 == 0:
        plista.append(valor)
    elif valor % 2 == 1 or valor == 1:
        ilista.append(valor)
    if r == 'n':
        break

print(lista)
print(plista)
print(ilista)'''


num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(num)
print(pares)
print(impares)