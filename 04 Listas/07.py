"""
 07) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
number = list()
multiple = float()
for n in range(0, 5):
    number.append(int(input(f'Digite o {n}º número: ')))
print(f'A lista digitada foi {number}.\n'
      f'A soma dos numeros da lista é {sum(number)}')
for i in range(0, len(number)):
    if number[0] == number[i]:
        multiple = number[i]
    multiple *= number[i]
print(f'A multiplicação entre os números {str(number)} é {multiple}')
