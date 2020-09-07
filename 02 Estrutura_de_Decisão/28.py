"""
 28)O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
  cliente receberá ainda um desconto de 5% sobre o total da compra.
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    contendo as informações da compra:
        tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
print(f'{"Hipermercado Tabajara":~^50}\n{"="*50}')
print(f"{'Menu do dia':^40}\n{'~'*50}")
print(f"{'cod':5}{'Produto':15}{'Até 5Kg:':15}{'Acima de 5Kg:'}\n"
      f"{'1':5}{'File Duplo':15}{'R$ 4,90/kg':15}{'R$  5,80/Kg'}\n"
      f"{'2':5}{'Alcatra':15}{'R$ 5,90/kg':15}{'R$  6,80/Kg'}\n"
      f"{'3':5}{'Picanha':15}{'R$ 6,90/kg':15}{'R$  7,80/Kg'}\n{'~'*50}")
cod_c = int(input('Digite do codigo do produto: '))
preco = float()
carne = str()
if cod_c == 1:
    carne = 'File Duplo'
    peso = float(input(f'Quantos Kg de {carne}?: '))
    preco = 4.9
    if peso > 5:
        preco = 5.8
elif cod_c == 2:
    carne = 'Alcatra'
    peso = float(input(f'Quantos Kg de {carne}?: '))
    preco = 5.9
    if peso > 5:
        preco = 6.8
elif cod_c == 3:
    carne = 'Picanha'
    peso = float(input(f'Quantos Kg de {carne}?: '))
    preco = 6.9
    if peso > 5:
        preco = 7.8
v_total = preco*peso
v_desconto = v_total
print(f"{'Formas de pagamento':^30}\n"
      f"{'='*30}\n"
      f"{'cod':5}{'Opções'}\n"
      f"{'1':5}{'Cartão de Credito'}\n"
      f"{'1':5}{'Cartão Tabajara'}\n"
      f"{'3':5}{'Dinheiro'}")
cod_p = int(input('Digite o Código: '))
f_pag = str()
desconto = 'Sem desconto'
if cod_p == 1:
    f_pag = 'Cartão de Credito'
elif cod_p == 2:
    f_pag = 'Cartão Tabajara'
    desconto = '5%'
    v_desconto = v_total - (v_total * .05)
elif cod_p == 3:
    f_pag = 'Dinheiro'

print(f"\n{'Cupom Fiscal':^50}\n{'-'*50}")
print(f"{'Tipo de carne:':25}{carne}\n"
      f"{'Quantidade de carne:':25}{peso:.2f}kg\n"
      f"{'Preço p/Kg:':25}R${preco:.2f}\n"
      f"{'Preço total':25}R${v_total:.2f}\n"
      f"{'Forma de pagamento':25}{f_pag}\n"
      f"{'Descontos':25}{desconto}\n"
      f"{'Total a pagar:':25}R${v_desconto:.2f}")
