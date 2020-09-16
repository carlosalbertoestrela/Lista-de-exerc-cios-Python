"""
 14) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
respostas = []
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
             "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
for p in range(len(perguntas)):
    while True:
        r = input(f'{perguntas[p]} [Sim/Não]')[0]
        if r.upper() in "SN":
            if r.upper() == 'S':
                respostas.append(r)
                break
            else:
                break
print('O interrogado é ', end='')
if len(respostas) < 2:
    print('Inocente')
elif len(respostas) == 2:
    print('Suspeito')
elif 2 < len(respostas) <= 4:
    print('o Cúmplice')
else:
    print('O Assacino!!')


