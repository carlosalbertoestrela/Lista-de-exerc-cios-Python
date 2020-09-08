"""
 21) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
  Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
num = int(input('Digite um número: '))
primo = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            primo = False
    print(f'O número {num} ', end='')
    if primo:
        print('é Primo')
    else:
        print('não é Primo')
else:
    print('Número inválido')