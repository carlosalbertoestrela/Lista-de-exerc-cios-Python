"""
 17) Faça um Programa que peça um número correspondente a um determinado ano e
 em seguida informe se este ano é ou não bissexto.
"""
ano = input("Digite o ano: ").strip()
ano_dezena = int(ano[-2] + ano[-1])
print(f'O ano {ano} ', end='')
if ano_dezena == 00:
    ano_dezena = int(ano[1:])
    if ano_dezena % 400 == 0:
        print('é Bissexto!')
    else:
        print('NÃO é Bissexto!')
elif ano_dezena % 4 == 0:
    print('é Bissexto!')
else:
    print('NÃO é Bissexto!')

