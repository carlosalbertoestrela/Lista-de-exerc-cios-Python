"""
 13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
 elevado ao segundo número. Não utilize a função de potência da linguagem
"""
base = int(input('Digite a BASE: '))
expo = int(input('Digite o EXPOENTE: '))
result = int()
for n in range(1, expo):
    if n == 1:
        result = base * base
    else:
        result *= base
print(f"{base} elevado a {expo} é igual a {result}")
