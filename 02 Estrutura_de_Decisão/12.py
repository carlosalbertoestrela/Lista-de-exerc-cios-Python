"""
 12) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
 que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
 Salário Bruto menos os descontos. O programa deverá pedir ao usuário o
 valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
hora_trabalhada = int(input('Horas trabalhadas: '))
valor_hora = float(input('Valor da hora de trabalho: R$'))
salario_bruto = valor_hora * hora_trabalhada
sindicato = salario_bruto * .03
fgts = salario_bruto * .11
imposto_renda = float()
if salario_bruto <= 900:
    imposto_renda = 0
    val = 'Isento'
elif salario_bruto <= 1500:
    imposto_renda = salario_bruto * .05
    val = 5
elif salario_bruto <= 2500:
    imposto_renda = salario_bruto * .1
    val = 10
else:
    imposto_renda = salario_bruto * .2
    val = 20
salario_liquido = salario_bruto - (imposto_renda + sindicato)

print(f"""
       Salário bruto: ({hora_trabalhada} * R${valor_hora:.2f}) : R$ {salario_bruto:.2f}
       (-) IR ({val}%)                   : R$ {imposto_renda:.2f}
       (-) Sindicato (3%)            : R$ {sindicato:.2f}
       Total de descontos            : R$ {sindicato + imposto_renda:.2f}
       Salário Liquido               : R$ {salario_liquido:.2f}
       """)
