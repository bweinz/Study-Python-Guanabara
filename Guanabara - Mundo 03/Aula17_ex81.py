#Crie um programa que leia varios numeros e coloque em uma lista
'''
A) quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente
c) Se o valor 5 foi digitado e este ou não na lista
'''

'''valor = 0
lista = []
r = ''
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    r = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    cont += 1
    if r != 'n' and r != 's':
        print('Digite um valor valido:')
    elif r == 'n':
        break

lista.sort(reverse=True)

print(f'Resposta A) {cont}'
      f'\nResposta B) {lista}')

if 5 in lista:
    print('O valor 5 faz parte desta lista!')
else:
    print('O Valor 5 não foi encontrado na lista')'''

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer Continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'A ordem descrescente é {valores}')

if 5 in valores:
    print('O valor 5 está nos valores')
else:
    print('O valor 5 não faz parte da lista')