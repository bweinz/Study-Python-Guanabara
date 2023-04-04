#Ex 57 faça um programa que leia o sexo de uma pessoa mas só aceite os valores M ou F caso esteja errado peça a digitação novamente até ter um valor correto

sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]

while sexo not in 'mMfF':
    sexo = str(input('Dados inválidos. por favor informe seu sexo: ')).upper()

print(f'Sexo {sexo} Foi registrado com sucesso')