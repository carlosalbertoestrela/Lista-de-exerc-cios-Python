"""
 21) Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
     uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
     quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
valor = int(input('Digite o valor a ser sacado: [min: R$10, max: R$600] '))
s = str()
if 10 <= valor <= 600:
    n_100 = valor // 100
    n_50 = (valor - (n_100*100)) // 50
    n_10 = (valor - ((n_100*100)+(n_50*50))) // 10
    n_1 = (valor - ((n_100*100)+(n_50*50) + (n_10*10))) // 1
    print(f'Para sacar o valor R${valor:.2f}, serão sacadas', end='')
    if n_100 > 0:
        if n_100 > 1:
            s = 's'
        else:
            s = ''
        print(f' {n_100} nota{s} de R$100', end='')
        if (n_50 > 0 and n_10 > 0) or (n_50 > 0 and n_1 > 0) or (n_10 > 0 and n_1 > 0):
            print(',', end='')
        elif n_50 > 0 or n_10 > 0 or n_1 > 0:
            print(' e', end='')
        else:
            print('.')
    if n_50 > 0:
        if n_50 > 1:
            s = 's'
        else:
            s = ''
        print(f' {n_50} nota{s} de R$50', end='')
        if n_10 > 0 and n_1 > 0:
            print(',', end='')
        elif n_10 > 0 or n_1 > 0:
            print(' e', end='')
        else:
            print('.')
    if n_10 > 0:
        if n_10 > 1:
            s = 's'
        else:
            s = ''
        print(f' {n_10} nota{s} de R$10', end='')
        if n_1 > 0:
            print(' e', end='')
        else:
            print('.')
    if n_1 > 0:
        if n_1 > 1:
            s = 's'
        else:
            s = ''
        print(f' {n_1} nota{s} de R$1.')
else:
    print('Valor inválido')
