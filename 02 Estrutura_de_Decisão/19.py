"""
 19) Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
  326 = 3 centenas, 2 dezenas e 6 unidades
  12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input('Digite um númro menor que 1000: '))
if 0 > num > 1000:
    print('Número inválido')
else:
    cent = num // 100
    dezn = (num - (cent * 100)) // 10
    unid = (num - (cent * 100) - (dezn * 10)) // 1
    p_c = p_d = p_u = ''
    if cent > 1:
        p_c = 's'
    if dezn > 1:
        p_d = 's'
    if unid > 1:
        p_u = 's'
    print(f'O número {num} tem', end='')
    if cent > 0:
        print(f' {cent} cemtena{p_c}', end='')
        if dezn > 0 and unid > 0:
            print(',', end='')
        elif dezn > 0 or unid > 0:
            print(' e', end='')
        else:
            print('.')
    if dezn > 0:
        print(f' {dezn} dezena{p_d}', end='')
        if unid > 0:
            print(' e', end='')
        else:
            print('.')
    if unid > 0:
        print(f' {unid} unidade{p_u}.')
