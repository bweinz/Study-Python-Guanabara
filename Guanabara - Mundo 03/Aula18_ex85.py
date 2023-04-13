#Crie um programa onde o usuário possa digitar sete valores numéricos
#cadastre-os em uma lista unica que mantenha separados os valores pares e impares
#no final mostre os valores pares e impares em ordem crescente


num = [[], []]
valor = 0

for c in range (1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)
num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]} ')
print(f'Os valores impares digitados foram: {num[1]}')

'''par = []
imp = []
princ = []

for i in range(0, 7):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 == 1:
        imp.append(valor)

par.sort()
imp.sort()

print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {imp}')'''


