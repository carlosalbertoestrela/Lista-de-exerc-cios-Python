"""
 09) Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
num1 = int(input('Digite o primeiro número: '))
maior = menor = meio = num1
num2 = int(input('Digite o segundo número: '))
if num2 > maior:
    meio = maior
    maior = num2
elif num2 < menor:
    meio = menor
    menor = num2
else:
    meio = num2
num3 = int(input('Digite o teceiro número: '))
if num3 > maior:
    meio = maior
    maior = num3
elif num3 < menor:
    meio = menor
    menor = num3
else:
    meio = num3

print(f'Os números digitados em ordem decrescente são: {maior}, {meio} e {menor}')
