"""
 11) Altere o programa anterior para mostrar no final a soma dos números.
"""
i = int(input('Digite o número de INICIO: '))
f = int(input('Digite o número para o FINAL: '))
print(f'Os números entre {i} e {f} são: ', end='')
soma = int()
if i > f:
    p = -1
    for num in range((i-1), f, p):
        print(f'{num}, ', end='')
        soma += num
else:
    p = 1
    for num in range(i+1, f, p):
        print(f'{num}, ', end='')
        soma += num
print('fim')
print(f'A soma desse intervalo é {soma}')
