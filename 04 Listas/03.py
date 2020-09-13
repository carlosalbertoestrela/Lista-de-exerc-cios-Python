"""
 03) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
notas = list()
for i in range(1, 5):
    nota = float(input(f'Digirte a {i}ª nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f'As notas digitadas foram: {notas} e sua média é {media:.1f}')