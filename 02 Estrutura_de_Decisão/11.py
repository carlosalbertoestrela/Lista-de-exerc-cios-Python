"""
 11) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input('Digite o salário do colaborador: R$'))
ajuste = int()
ajustado = salario
if salario >= 1500.00:
    ajustado += salario * .05
    ajuste = 5
elif 700.0 <= salario < 1500.0:
    ajustado += salario * .1
    ajuste = 10
elif 280.0 < salario < 700.0:
    ajustado += salario * .15
    ajuste = 15
else:
    ajustado += salario * .20
    ajuste = 20
print(f'O salario de R${salario:.2f} terá o aumento de R${salario * (ajuste/100):.2f} '
      f'equivalente a {ajuste}% e passará a ser R${ajustado:.2f}')
