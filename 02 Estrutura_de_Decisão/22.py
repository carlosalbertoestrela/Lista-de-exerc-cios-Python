"""
 21) Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
 Dica: utilize o operador módulo (resto da divisão).
"""
num = int(input('Digite um número: '))
print(f'{num} é ', end='')
if num % 2 == 0:
    print('PAR!!')
else:
    print('IMPAR')
