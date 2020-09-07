"""
 07) Faça um programa que leia 5 números e informe o maior número.
"""
maior = int()
for n in range(1, 6):
    num = int(input(f'Digite o {n}º número: '))
    if num > maior:
        maior = num
print(f'o número {maior} foi o maior')

