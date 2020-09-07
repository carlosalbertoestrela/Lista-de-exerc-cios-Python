"""
 16) A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
 Faça um programa que gere a série até que o valor seja maior que 500.
"""
a = b = cont = 1
print('Sequencia de Fibonacci: 0, ', end='')
while True:

    if cont % 2 == 1:
        print(f'{a}, ', end='')
        if a > 500:
            break
        a = a + b
        cont += 1
    else:
        print(f'{b}, ', end='')
        b = a + b
        cont += 1
print('fim')
