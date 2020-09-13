"""
 06) Faça um Programa que peça as quatro notas de 10 alunos,
 calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
medias = list()
notas = float()
for a in range(0, 10):
    print(f'{a+1}º Aluno: ')
    for n in range(0, 4):
        nota = float(input(f'  Digite a {n+1}ª nota: '))
        notas += nota
    media = notas / 4
    medias.append(media)
    notas = 0
print(f"{'Médias!':^30}\n{'='*30}")
for a, m in enumerate(medias):
    print(f'   {a+1}º Aluno: {m}')

