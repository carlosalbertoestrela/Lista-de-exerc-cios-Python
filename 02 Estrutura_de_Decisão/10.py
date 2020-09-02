"""
 10) Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
 Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print('Qual seu turo:\n -M > Matutino\n -V > Vespertino\n -N > Noturno')
turno = str(input('Resposta: ')).upper().strip()[0]
if turno in 'MVN':
    if turno == 'M':
        print('Bom Dia!')
    elif turno == 'V':
        print('Boa Tarde!')
    else:
        print('Boa Noite!')
else:
    print('Valor inválido!!')
