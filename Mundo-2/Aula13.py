'''
#Conceito parte1 Laços For:
print('Agora com laço: ')
for c in range (0, 3):
    print('Oi')
print('fim')
#obs: no range o segundo valor sempre será contado com -1 ou seja, cada (0, 1, 2) não conta 3 pois 3-1 para na posição 2

#Contando ao contrario:
for b in range (6, 0, -1):
    print(b)
#obs: pra contar ao contrario dizemos que o terceiro valor é a o valor da iteração ou seja, começamos em 6 diminuindo 1 em 1

#Contando Pulando casa:
for a in range (0, 7, 2):
    print(a)
#obs: Irá pular de 2 em 2 na contagem: 0,2,4,6
'''
#Somando com For e input
s = 0
for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n                                  #mesma coisa que: (s = s + n)
print(f'A soma dos valos é igual a {s}')