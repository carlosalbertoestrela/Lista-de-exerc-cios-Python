"""
 18) Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
data = input('Digite a data: dd/mm/aaaa: ')
print(' Dada ', end='')
fevereiro = False
if len(data) == 10 and data[2] == '/' == data[5]:  # primeira validação.
    if int(data[8:]) != 00 and int(data[8:]) % 4 == 0:  # testa se é bissexto.
        fevereiro = True
    elif int(data[8:] == 00) and int(data[7:]) % 4 == 0:
        fevereito = True
    if int(data[3:5]) <= 12 and int(data[3:5]) > 0:  # testa se o campo "mm" tem corresponde aos 12 meses.
        if int(data[3:5]) == 2:  # testa se é fevereiro.
            if fevereiro and 29 >= int(data[0:2]) > 0:  # testa se é bissexto.
                print('VALIDA!')
            else:
                print('INVÁLIDA')
            if 28 >= int(data[0:2]) > 0:
                print('VALIDA')
            else:
                print('INVÁLIDA')
        elif int(data[3:5]) == 1 or 3 or 5 or 7 or 8 or 10 or 12:  # testar meses com 31 dais: 1, 3, 5, 7, 8, 10, 12
            if 31 >= int(data[0:2]) > 0:
                print('VALIDA')
            else:
                print('INVÁLIDA')
        else:
            if 30 >= int(data[0:2]) > 0:
                print('VALIDA')
            else:
                print('INVÁLIDA')
    else:
        print('INVÁLIDA')
else:
    print('INVÁLIDA')
