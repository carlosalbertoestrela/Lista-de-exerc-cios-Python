"""
 25) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"
"""
print(f'{"DETETIVE":=^30}')
print('Responda com sim ou não:')
p1 = str(input('Telefonou para a vítima? ')).upper().strip()[0]
p2 = str(input('Esteve no local do crime? ')).upper().strip()[0]
p3 = str(input('Mora perto da vítima? ')).upper().strip()[0]
p4 = str(input('Devia para a vítima? ')).upper().strip()[0]
p5 = str(input('Já trabalhou com a vítima? ')).upper().strip()[0]
score = int()
investigado = str()
if p1 == 'S':
    score += 1
if p2 == 'S':
    score += 1
if p3 == 'S':
    score += 1
if p4 == 'S':
    score += 1
if p5 == 'S':
    score += 1
if score < 2:
    investigado = 'Inocente'
elif score == 2:
    investigado = 'Suspeito'
elif 2 < score <= 4:
    investigado = 'um Cumplice'
else:
    investigado = 'o Assassino'
print(f'O investigado é {investigado}')
