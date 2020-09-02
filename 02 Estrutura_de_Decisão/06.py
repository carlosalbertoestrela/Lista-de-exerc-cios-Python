"""
 06) Faça um Programa que leia três números e mostre o maior deles.
"""
num1 = int(input('Digite o primeiro número: '))
maior = num1
num2 = int(input('Digite o segundo número: '))
if num2 > maior:
    maior = num2
num3 = int(input('Digite o terceito número: '))
if num3 > maior:
    maior = num3
print(f'O maior número digitado foi: {maior}')
