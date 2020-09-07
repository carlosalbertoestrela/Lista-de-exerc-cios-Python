"""
 14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
 números pares e a quantidade de números impares.
"""
impar = par = int()
for n in range(1, 11):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Foram digitados {impar} números impares e {par} números pares!')
