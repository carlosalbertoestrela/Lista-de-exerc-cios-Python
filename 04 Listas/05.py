"""
 05) Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
 Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
numeros = list()
pares = list()
impares = list()
for n in range(1, 21):
    num = int(input(f'Digite o {n} número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    numeros.append(num)
print(f'A lista de números digitados foi:\n'
      f'{numeros}\n'
      f'Pares:\n'
      f'{pares}\n'
      f'Impares:\n'
      f'{impares}')
