#  7) Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

comprimento = float(input('Digite o comprimento do quadrado: '))
altura = float(input('Digite a altura do quadrado: '))
area = comprimento * altura
print(f'A area do quadrado de {altura}x{comprimento} é {area:.2f} eseu dobor é {area*2:.2f}')
