#  7) Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

lado = float(input('Digite um lado do quadrado: '))
area = lado**2
print(f'A area do quadrado de {lado}x{lado} é {area:.2f} eseu dobor é {area*2:.2f}')
