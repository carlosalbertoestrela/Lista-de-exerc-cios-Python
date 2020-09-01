# 11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

int1 = int(input('Digite um número INTEIRO: '))
int2 = int(input('Digite outro número INTREIRO: '))
real = float(input('Digite um número REAL: '))
print(f'A soma do dobro de {int1} com a metade de {int2} é {(int1*2) + (int2/2)}!')
print(f'A soma do triplo de {int1} com {real} é {(int1 * 3) + real}!')
print(f'{real} elevado ao cubo é {real**3:.1f}!')