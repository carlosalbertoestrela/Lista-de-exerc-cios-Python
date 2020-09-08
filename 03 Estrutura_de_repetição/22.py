"""
 22) Altere o programa de cálculo dos números primos, informando,
 caso o número não seja primo, por quais número ele é divisível.
"""
num = int(input('Digite um número: '))
primo = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if not primo:
        for n in range(1, num + 1):
            if num % n == 0:
                if n == num:
                    print(f' e ', end='')
                elif n != num and n != 1:
                    print(', ', end='')
                print(f'{n}', end='')

        print(f' são os divizores de {num}, Portanto ele não é3 Primo')
    else:
        print(f'{num} é primo!')

