# 9) Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

tf = float(input('Temperatura em ºF: '))
tc = 5 * ((tf-32) /9)
print(f'ºF {tf} = ºC {tc:.1f}')
