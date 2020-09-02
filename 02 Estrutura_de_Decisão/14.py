"""
 14) Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
 e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2+nota1) / 2
conceito = str()
if 9 <= media <= 10:
    conceito = "A"
elif 7.5 <= media < 9:
    conceito = 'B'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 4 <= media < 6:
    conceito = 'D'
elif 0 <= media < 4:
    conceito = 'E'
if conceito in "ABC":
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f'{"Resumo do aluno":-^25}')
print(f'  Notas: {nota1} e {nota2}\n  Média: {media}\n  Situação: {situacao}\n  Conceito: {conceito}')
