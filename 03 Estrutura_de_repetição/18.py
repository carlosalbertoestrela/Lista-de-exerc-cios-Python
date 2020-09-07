"""
 18) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
maior = menor = soma = cont = 0
while True:
    num = int(input('Digite um número: (0 para parar) '))
    if soma == 0:
        maior = menor = num
    if num == 0:
        break
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
print(f'O MAIOR número digitado foi {maior}\n'
      f'O MENOR número digitado foi {menor}\n'
      f'A SOMA dos números digitados é {soma}')
