"""
 01) Faça um Programa que peça dois números e imprima o maior
"""
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}!')
elif n1 < n2:
    print(f'{n2} é maior que {n1}!')

else:
    print(f'{n1} e {n2} são iguais')
