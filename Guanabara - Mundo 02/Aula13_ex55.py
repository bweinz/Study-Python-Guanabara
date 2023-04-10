#Ex55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos:

pessoas = []


for n in range (1, 6):
    peso = float(input('Digite seu peso: '))
    pessoas.append(peso)
    maior_peso = max(pessoas)
    menor_peso = min(pessoas)
print(f'à pessoa com o maior peso possui: {maior_peso} kgs e a pessoa mais leve pesa {menor_peso} kgs')


pessoas2[85.6, 90.2, 48.9, 70.7, 65.5]