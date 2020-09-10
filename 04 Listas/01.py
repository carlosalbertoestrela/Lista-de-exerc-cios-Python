"""
 01) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
numeros = list()
for i in range(1, 6):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)
print(f'Os números digitados foram: {sorted(numeros)}')
