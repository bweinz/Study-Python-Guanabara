#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario:
'''
Quantidade de notas
a maior nota
a menor nota
a média da turma
a situação(opcional)

'''

'''def notas(*num, sit=False):
    dicionario = {}
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = sum(num) / len(num)
    if sit:
        if dicionario['média'] < 5:
            dicionario['situação'] = 'Pessimo'
        elif dicionario['média'] < 7:
            dicionario['situação'] = 'Em Alerta Manolo'
        elif dicionario['média'] < 9:
            dicionario['situação'] = 'Bom'
        else:
            dicionario['situação'] = 'Nerd do Caraio'
        print(dicionario)
    return dicionario


resp = notas(9, 9, 10, 10)'''


#Resolução Guanabara

def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)