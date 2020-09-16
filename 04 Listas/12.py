"""
 12) Foram anotadas as idades e alturas de 30 alunos.
 Faça um Programa que determine quantos alunos com mais de 13 anos
 possuem altura inferior à média de altura desses alunos.
"""
from random import randrange
altura = list()
idade = list()
for n in range(30):
    altura.append((randrange(100, 230)/100))
    idade.append(randrange(1, 90))
media_altura = sum(altura) / 30
cont = int()
for iten in range(len(altura)):
    if idade[iten] >= 13 and altura[iten] > media_altura:
        cont += 1
print(f'{cont} alunos tem mais de 13 anos e altura acima de {media_altura:.2f}m')
