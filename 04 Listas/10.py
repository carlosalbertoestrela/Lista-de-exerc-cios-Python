"""
 10) Faça um Programa que leia dois vetores com 10 elementos cada.
 Gere um terceiro vetor de 20 elementos,
 cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
vetor1 = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
vetor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor3 = list()
for i in range(0, len(vetor1)):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(f'{vetor1}\n'
      f'{vetor2}\n'
      f'{vetor3}\n')
