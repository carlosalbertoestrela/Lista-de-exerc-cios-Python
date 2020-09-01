# 12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite sua altura (em cm): '))
ideal = (72.7 * (altura/100)) - 58
print(f'O peso ideal para uma pessoa de {altura / 100:.2f}m é {ideal:.2f}Kg.')
