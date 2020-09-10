"""
 25) Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a
 média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem,
  adulta ou idosa, conforme a média calculada.
"""
cont = 0
turma = media_turma = 0
while True:
    cont += 1
    idade = int(input(f'Digite a idade do {cont}º participante: '))
    turma += idade
    continuar = str(input('Pressione "ENTER" para continuar ou "N" para parar: ')).upper()
    if continuar == 'N':
        break
media_turma = turma / cont
print(f'Com média de idade {media_turma:.1f} a  turma é: ', end='')
if 0 < media_turma <= 25:
    print('Jovem')
elif 26 <= media_turma <= 60:
    print('Adulta')
elif 60 < media_turma < 150:
    print('Idosa')
else:
    print('Média inválida')
