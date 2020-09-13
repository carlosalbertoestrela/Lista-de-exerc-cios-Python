"""
 04) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
letras = list()
for i in range(1, 11):
    letra = str(input('Digite um caractere: ')).upper()[0]
    if letra not in "AEIOU":
        letras.append(letra)
print(f'Foran digitadas {len(letras)} consoantes e elas foram: ', end='')
for i in range(0, len(letras)):
    if i != len(letras) - 1 and  i != 0:
        print(', ', end='')
    elif i < len(letras) and i != 0:
        print(' e ', end='')
    print(f'{letras[i]}', end='')
