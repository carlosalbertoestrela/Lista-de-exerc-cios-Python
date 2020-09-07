"""
 19) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
maior = menor = soma = cont = 0
while True:
    while True:
        num = int(input('Digite um número: (0 para parar) '))
        if 0 <= num <= 1000:
            break
        else:
            print('número inválido')
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
