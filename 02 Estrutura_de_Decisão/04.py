"""
 04) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = str(input('Digite uma letra: ')).strip().upper()[0]
if letra in 'AÀÁÂÃEÈÉÊIÌÍÎOÒÓÔÕUÚÙÛ':
    print(f'{letra} é uma VOGAL!')
else:
    print(f'{letra} é uma CONSOANTE!')
