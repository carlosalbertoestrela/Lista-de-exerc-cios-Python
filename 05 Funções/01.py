"""
 01) Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""


def cont_print(num):
    for n in range(num+1):
        print(f'{n}' * n)


cont_print(int(input('Digite um número: ')))
