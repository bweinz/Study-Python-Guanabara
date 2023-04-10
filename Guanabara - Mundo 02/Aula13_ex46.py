#ex 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0 com uma pausa de 1 segundo entre elas:

import time

for fogos in range (10, -1, -1):
    time.sleep(0.5)
    print(fogos)
print('Feliz ano novo \U0001F386')
