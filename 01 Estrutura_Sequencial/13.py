# 13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite sua altura (em cm): '))
idealH = (72.7 * (altura/100)) - 58
idealM = (62.1 * (altura/100)) - 44.7
print(f'O peso ideal para {altura/100}m é: {idealH:.2f}Kg para Homens e {idealM:.2f}Kg para mulheres')