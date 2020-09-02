"""
 07) Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
num1 = int(input('Digite o primeiro número: '))
menor = maior = num1
num2 = int(input('Digite o segundo número: '))
if num2 < menor:
    menor = num2
if num2 > maior:
    maior = num2
num3 = int(input('Digite o terceito número: '))
if num3 < menor:
    menor = num3
if num3 > maior:
    maior = num3
print(f'O meior número digitado foi: {maior}\nO menor número digitado foi: {menor}')
