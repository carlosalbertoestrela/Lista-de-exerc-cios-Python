"""
 23) Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
 Dica: utilize uma função de arredondamento.
"""
num = str(input('Digite um número: '))
print(f'{num} é ', end='')
if ',' in num or '.' in num:
    num = num.replace(",", ".")
    print('Decimal')
else:
    print('Inteiro')
