"""
 08) Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
soma = float()
for n in range(1, 6):
    num = float(input(f'Digite o {n}º número: '))
    soma += num
media = soma / 5
print(f'A soma dos números digitados foi {round(soma)} e a média {round(media)}!')
