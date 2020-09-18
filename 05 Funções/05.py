"""
 05) Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa
em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""


def somaImposto(taxa, num):
    t = num  * (taxa / 100)
    c = num + t
    return c


taxa = float(input('Digite a taxa (%): '))
custo = float(input('Digite o custo: R$ '))
print(f'O custo atualizado é {somaImposto(taxa, custo):.2f}')
