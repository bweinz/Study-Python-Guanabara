#Tuplas:

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)       #Tudo
print(lanche[0])    #Hamburguer
print(lanche[1:3])   #Suco, Pizza (ignora o ultimo)
print(lanche[2: ])   #Pizza, Pudim (do 2 até o ultimo)
print(lanche[ :2])   #Hamburguer, Suco (ignora o 2)
print(lanche[-1])    ##Pudim (ultimo valor)
print(len(lanche))   #4
print(sorted(lanche)) #Mostra em ordem alfabetica

'''lanche[1] = 'banana''' #dá error por não podem mudar a variavel em uma tupla

for comida in lanche:                       #Quando não precisa do numero de contagem
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')    #o contador faz com que conte INCLUSIVE o ultimo valor

for cont in range (0, len(lanche)):          #Usando o contador:
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

for pos, comida in enumerate(lanche):         #Usando o contador: Usando o Contador com in
    print(f'Eu vou comer {comida} na posição {pos}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b    #( 2, 5, 4, 5, 8, 1, 2)

print(len(c))  #7
print(c.count(5)) #quantas vezes está aparecendo o numero 5
print(c.index(8))  #em que posição está o 8 no index (pega o primeiro se houver repetido colocamos:
print(c.index(5,1))  #a posição do 5, mas não o primeiro valor [0], o segundo [1]

pessoa = ('Gustavo', 39, 'M', 99.88)  #Pode misturar diversos dados
del(pessoa)    #podemos apagar uma tupla inteira com Del
