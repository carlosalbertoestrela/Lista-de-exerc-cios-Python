"""
 11) Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
vetor3 = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'setimo', 'oitavo', 'nono', 'décimo']
vetor4 = list()
for i in range(0, len(vetor1)):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print(f"{vetor1}\n{vetor2}\n{vetor3}\n{vetor4}")
