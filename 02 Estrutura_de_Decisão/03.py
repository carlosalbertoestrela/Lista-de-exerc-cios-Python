"""
 03) Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = str(input('Sexo: [M/F] ')).strip()[0]
if sexo in 'MmFf':
    if sexo in 'mM':
        print('M - Masculino.')
    else:
        print('F - Feminino.')
else:
    print('Sexo inválido!!')
