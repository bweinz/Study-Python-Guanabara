#Crie um programa que tenha uma tupla com várias palavras não usar acentos. depois disso você deve mostrar para cada palavra quais são as suas vogais

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis')

for p in palavras:
    print(f'\n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')