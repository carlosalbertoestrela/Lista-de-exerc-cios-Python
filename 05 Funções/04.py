"""
 04) Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def teste_p_n(num):
    if num > 0:
        return 'P'
    else:
        return 'N'


n = int(input('Digite um número para saber se é N - negativo, P - positivo: '))
print(f'O resultado é: {teste_p_n(n)}')
