"""
 08) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
 sabendo que a decisão é sempre pelo mais barato.
"""
produto1 = float(input('Digite o valor do primeiro produto: R$ '))
compra = produto1
cont = 1
produto2 = float(input('Digite o valor do segundo produto: R$ '))
if compra > produto2:
    compra = produto2
    cont = 2
produto3 = float(input('Digite o valor do terceiro produto: R$ '))
if compra > produto3:
    compra = produto3
    cont = 3
print(f'O melhor produto para comprar é o {cont}º por custar R${compra:.2f}!')
