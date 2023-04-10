#Ex 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final mostre os 10 primeiros termos dessa progressão

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro + (10 -1) * razao #termos = t2 * 10    ---- Minha FOrmula---
for n in range (primeiro, termo + razao , razao):
    print(n, end=' > ')
