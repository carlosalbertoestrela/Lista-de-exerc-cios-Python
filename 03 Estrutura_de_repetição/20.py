"""
 20) Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
  fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""
while True:
    num = int(input('Difite um número para saber sue fatorial: (0 para sair) '))
    if num == 0:
        print('Programa finalizado')
        break
    cont = num
    fator = 1

    if 0 < num <= 16:
        print(f'{num}! = ', end='')
        for i in range(cont):
            fator *= cont
            if cont == 1:
                print(f'{cont} = ', end='')
            else:
                print(f'{cont}.', end='')
            cont -= 1
        print(f'{fator}')
    else:
        print('Número inválido! tente novamente.')



