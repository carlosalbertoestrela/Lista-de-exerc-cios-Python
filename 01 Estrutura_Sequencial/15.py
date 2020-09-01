# 15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
#    * + Salário Bruto : R$
#    * - IR (11%) : R$
#    * - INSS (8%) : R$
#    * - Sindicato ( 5%) : R$
#    * = Salário Liquido : R$

salarioHora = float(input('Salário hora: R$'))
horasMes = int(input('Horas trabalhadas no mês: '))
bruto = salarioHora * horasMes
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - (ir + inss + sind)
print(f' - Salário bruto =    R${bruto:.2f}')
print(f' - Imposto de renda = R${ir:.2f}')
print(f' - INSS =             R${inss:.2f}')
print(f' - Sindicato =        R${sind:.2f}')
print(f' - Salário liquido =  R${liquido:.2f}')
