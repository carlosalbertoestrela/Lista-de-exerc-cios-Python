"""
 26) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
 calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
 gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
print(f'{"Posto Tabajara":~^30}')
print('tipo de combustivél:\n  (G) Gasolina R$2,50/L\n  (A) Álcool R$1,90/L')
combustivel = str(input('Sua escolha: ')).strip().upper()[0]
litro = float(input('Quantos litros deseja abastecer? '))
v_litro = float()
v_desconto = float()
n_combustivel = str()
if combustivel == 'G':
    n_combustivel = 'Gasolina'
    v_litro = 2.5
    v_desconto = 4
    if litro > 20:
        v_desconto = 6
elif combustivel == 'A':
    n_combustivel = 'Álcool'
    v_litro = 1.9
    v_desconto = 3
    if litro > 20:
        v_desconto = 5
else:
    print('valor inválido')
v_total = (v_litro - (v_litro * (v_desconto/100))) * litro
print(f'Comprando {litro}L de {n_combustivel}, custando R${v_litro:.2f}/L com desconto de {v_desconto}%/L:\n'
      f'O total a ser pafo é R${v_total:.2f}.')
