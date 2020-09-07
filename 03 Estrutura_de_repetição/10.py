"""
 10) Faça um programa que receba dois números inteiros e gere os números
  inteiros que estão no intervalo compreendido por eles.
"""
i = int(input('Digite o número de inicio: '))
f = int(input('Digite o número final: '))
if i > f:
    p = -1
else:
    p = 1
print(f'Os númeors no intervalo entre {i} e {f} são: ', end='')
for num in range((i-1), f, p):
    print(f'{num}, ', end='')
print('fim')
