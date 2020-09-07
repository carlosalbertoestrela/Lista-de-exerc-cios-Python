"""
 15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
 Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
termo_final = int(input('Até que termo deseja ver a sequencia de Fibonacci? '))
a = 1
b = 1
print(f'Sequencia de Fibonacci até o {termo_final}º termo: ', end='')
for n in range(1, termo_final+1):
    if n % 2 == 1:
        print(f'{a}, ', end='')
        a = a + b
    else:
        print(f'{b}, ', end='')
        b = a + b
print('fim')
