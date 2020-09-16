"""
 09)Faça um Programa que leia um vetor A com 10 números inteiros,
 calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
numeros = list()
soma = float()
for n in range(0, 10):
    while True:
        num = input(f'Digite o {n+1}º número: ')
        if num.isnumeric():
            numeros.append(int(num))
            break
        else:
            print('deve ser digitado um número. Tente novamente.')
for i in range(0, len(numeros)):
    soma += numeros[i] ** 2
print(f'a soma dos quadrados de {str(numeros).replace(",", "² + ").replace("]", "²").replace("[", "")} é {soma}')
