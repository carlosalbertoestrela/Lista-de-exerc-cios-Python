"""
 24) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print(f'Escolha a operação\n'
      f' {"Divisão":20}( / )\n'
      f' {"Multiplicação":20}( X )\n'
      f' {"Subtração":20}( - )\n'
      f' {"Adição":20}( + )')
escolha = str(input('Sua escolha: ')).strip().upper()[0]
if escolha == '/':
    resultado = num1 / num2
elif escolha == 'X':
    resultado = num1 * num2
elif escolha == '-':
    resultado = num1 - num2
elif escolha == '+':
    resultado = num1 + num2
print(f'O resultado da operação ({num1} {escolha} {num2}) é {resultado:.2f}.')
print(f'O número {resultado:.2f} é ', end='')
if resultado % 2 == 0:
    print('PAR, ', end='')
else:
    print('IMPAR, ', end='')
if resultado >= 0:
    print('POSITIVO e ', end='')
else:
    print('NEGATIVO e ', end='')
if resultado // 1 == resultado:
    print('INTEIRO!', end='')
else:
    print('DECIMAL', end='')





