#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o numero já exista lá dentro, ele não será adicionado
#no Final Serão exibidos todos os valores únicos digitados em ordem crescente.

'''numeros = []

while True:
    n = int(input('Digite um valor: '))                     #N recebe o valor digitado
    if n not in numeros:                                    #Se o valor digitado não estiver na lista
        numeros.append(n)                                   #Adicione-o
        print('Valor Adicionado com Sucesso')
    else:                                                   #caso já tenha na lista faça:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Deseja continuar [S/N]')).split()[0]     #R recebe a resposta do usuario
    if r in 'nN':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')


print(numeros)'''

numeros = []

while True:
    n = int(input('Digite um valor: '))                     #N recebe o valor digitado
    if n not in numeros:                                    #Se o valor digitado não estiver na lista
        numeros.append(n)                                   #Adicione-o
        print('Valor Adicionado com Sucesso')
    else:                                                   #caso já tenha na lista faça:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Deseja continuar [S/N]')).split()[0]     #R recebe a resposta do usuario
    if r in 'nN':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')


print(numeros)