#EX 53: crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Escreva uma frase: ')).strip().upper()   #strip() corta a frase em palavras
palavras = frase.split()                                    #Salva as palavras de frase em um varaviavel chamada palavras, que vira uma lista
palavras_juntas = ''.join(palavras)                         #junta as palavras ('' fala pra adicionar sem espaçamento, o que colocar dentro de '' vai unir as palavras, ex '-' palavra1-palavra2)
inverso = ''

print(palavras)
print(palavras_juntas)

for letra in range(len(palavras_juntas) - 1, -1, -1):       # Quantidades de letras na frase escrita em palavra - 1, começando de traz para frente -1, contando de 1 em 1 de traz para frente -1
    inverso += palavras_juntas[letra]                       # Pega a letra que esta na posição inversa e vai adicionando na variavel inverso
print(inverso)

if inverso == frase:
    print('è um polindromo')
else:
    print('Não é um polindromo')

