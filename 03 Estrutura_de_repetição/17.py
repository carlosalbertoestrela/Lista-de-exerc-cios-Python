"""
 17) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
num = int(input('Digite um número: '))
resultado = int()
cont = num - 1
while cont != 0:
    if cont == num - 1:
        resultado += num * cont
        cont -= 1
    else:
        resultado *= cont
        cont -= 1
print(f"O fatorial de {num} é {resultado}")
