"""
 02) Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def print_cont_seq(num):
    for n in range(num+1):
        for i in range(1, n+1):
            print(f'{i} ', end='')
        print()


print_cont_seq(int(input('Digite um número: ')))
