"""
 27) Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
print(f'{"="*30}\n{"-- Orti-tabajara --":^30}\n{"="*30}')
print(f"{'Digite o peso em Kg: ':^25}")
maca = float(input(f'{"Maçã:":<10}Kg '))
morango = float(input(f'{"Morango:":<10}Kg '))
p_maca = 1.8
p_morango = 2.5
if maca > 5:
    p_maca = 2.2
if morango > 5:
    p_morango = 1.5
v_maca = p_maca * maca
v_morango = p_morango * morango
print(f'Comprando {maca:.2f}Kg de Maçã a R${p_maca:.2f} pagará por elas R${v_maca:.2f}')
print(f'Comprando {morango:.2f}Kg de Morango a R${p_morango:.2f} paragá por eles R${v_morango:.2f}')
print(f'Total a ser pago: R${v_maca + v_morango:.2f}')
