#Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()) no final mostre a lista ordenada na tela


lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:                             #Se C(posição) for 0, ou seja, se for o primeiro número digitado ou for maior que o ultimo numero da lista,
        lista.append(n)                                     #Apenas adicione no final da lista!
    else:
        pos = 0                                             #posição inicia em 0
            while pos < len(lista):                         #Enquanto posição for menor que o index da lista (quantidade de itens) (5)
            if n <= lista[pos]:                             #Se o numero digitado for menor ou igual o numero que corresponde a lista na posição atual
                lista.insert(pos, n)                        #Adiciona na posição atual o numero
                break
            pos += 1                                        #mudamos para proxima posição, até chegar em 5

print(lista)



