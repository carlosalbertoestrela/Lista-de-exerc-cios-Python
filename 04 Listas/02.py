"""
 02) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
numeros = list()
for i in range(1, 11):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)
numeros.sort(reverse=True)
print(f'A lista inversa de números digitados é {numeros}')
