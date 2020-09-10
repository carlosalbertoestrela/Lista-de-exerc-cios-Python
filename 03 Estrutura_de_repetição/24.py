"""
 24) Faça um programa que calcule o mostre a média aritmética de N notas.
"""
total = media = cont = 0
while True:
    cont += 1
    nota = float(input(f'digite a {cont}ª nota: '))
    total += nota
    conf = str(input('"N" para encerrar ou "ENTER" para continuar: ')).upper()
    if conf == 'N':
        break

media = total / cont
print(f'A média dos número digitados é {media}!')
