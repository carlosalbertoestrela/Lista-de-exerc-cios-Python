"""
 05) Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digire a segundda nota: '))
media = (nota1 + nota2) / 2
if 7 <= media < 10:
    print(f'APROVADO com média {media:.1f}')
elif media < 7:
    print(f'REPROVADO com média {media:.1f}')
elif media == 10:
    print(f'APROVADO COM DISTINÇÃO com média {media:.1f}')
elif media > 10:
    print('Média inválida!')
