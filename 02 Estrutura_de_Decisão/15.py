"""
 15)Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
 triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
        Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
        Triângulo Equilátero: três lados iguais;
        Triângulo Isósceles: quaisquer dois lados iguais;
        Triângulo Escaleno: três lados diferentes;
"""
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
triangulo = False
if (lado1 - lado2) < lado3 < (lado1 + lado2):
    if (lado3 - lado2) < lado1 < (lado3 + lado2):
        if (lado1 - lado3) < lado2 < (lado1 + lado3):
            triangulo = True
if triangulo:
    print(f"{lado1}, {lado2} e {lado3} podem formar um triângulo ", end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    elif lado1 != lado2 != lado3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print(f"{lado1}, {lado2} e {lado3} não podem formar um triângulo!")
