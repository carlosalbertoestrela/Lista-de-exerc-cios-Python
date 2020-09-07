"""
 05) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação
"""
pais_A = int(input('População pais A: '))
t_pais_A = float(input('Taxa de crescimento anual pais A: '))
pais_B = int(input('População pais B: '))
t_pais_B = float(input('Taxa de crescimento anual pais B: '))
anos = int()
if pais_A > pais_B:
    p1 = pais_A
    t1 = t_pais_A / 100
    p2 = pais_B
    t2 = t_pais_B / 100
    a = p1
    b = p2
else:
    p1 = pais_B
    t1 = t_pais_B / 100
    p2 = pais_A
    t2 = t_pais_A / 100
    a = p2
    b = p1
while p1 >= p2:
    p1 += p1 * t1
    p2 += p2 * t2
    anos += 1

print(f'Os paises levarão aproximadamente {anos} anos para se equivaler')
