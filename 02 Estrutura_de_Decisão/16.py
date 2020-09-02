"""
 16) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
 O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
from math import sqrt
a = int(input('Digite o valor de "a": '))
if a != 0:
    b = int(input('Digite o valor de "b": '))
    c = int(input('Digite o valor de "c": '))
    delta = (b**2) - ((4*a)*c)
    x = (b*-1)
    if delta == 0:
        print(f'O Delta é "{delta:.2f}"! A equação possui apenas uma raiz real: {sqrt(delta):.2f}')
    if delta > 0:
        print(f'O Delta "{delta:.2f}" é positivo ! A equação possui duas raizes reais: {sqrt(delta):.2f} e'
              f' {sqrt(delta)*-1:.2f}')
    else:
        print(f'Delta  {delta:.2f} é negativo! a equação não possui raizes reais!')
else:
    print('"A" não pode ser igual a "0", equação não é de segundo grau!')

