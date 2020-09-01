# 10) Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

tc = float(input('Temperatura em ºC: '))
tf = tc * 1.8 + 32
print(f'ºC {tc} = ºF {tf:.1f}')
