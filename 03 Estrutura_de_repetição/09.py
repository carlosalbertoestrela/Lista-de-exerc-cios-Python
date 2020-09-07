"""
 09) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
print('Impares entre 1 e 50 : ', end='')
for num in range(1, 51):
    if num % 2 == 1:
        print(f'{num}, ', end='')
print('fim')
