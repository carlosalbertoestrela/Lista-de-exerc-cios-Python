"""
 03) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def soma_3(n1=0, n2=0, n3=0):
    soma = n1 + n2 + n3
    return soma


print("DIgite tês números para soma-los: ")
n1 = int(input('1º: '))
n2 = int(input('2º: '))
n3 = int(input('3º: '))
print(f'{n1} + {n2} + {n3} = {soma_3(n1,n2,n3)}')
