'''def soma(a,b):
    print(f'A = {a} e B= {b}')
    s = a+b
    print(s)


#Programa Principal
soma(b=4, a=5)
soma(3,4)


def contador(*num):
   print(num)

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

'''
#listas:

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


#Desempacotamento:
def soma(*valores):
    soma = 0
    for numero in valores:
        soma += numero
    print(f'Somando os valores {valores} temos {soma}')

soma(5,2)
soma(2,9,4,2)