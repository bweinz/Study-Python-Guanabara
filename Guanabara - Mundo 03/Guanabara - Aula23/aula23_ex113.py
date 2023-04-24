#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possbilidade da digitação de um número de tipo invalido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('Erro: por favor, digite um numero inteiro válido')
            continue                            #continue rodando o while
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar nenhum numero.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('Erro: por favor, digite um numero inteiro válido')
            continue  # continue rodando o while
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar nenhum numero.')
            return 0
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
num2 = leiaFloat('Digite um valor Real')
print(f'O valor digitado foi {num2}')