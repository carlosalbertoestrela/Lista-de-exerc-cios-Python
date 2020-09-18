"""
 15) Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
 encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
 Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""
from time import sleep
notas = list()
cont = 0
while True:
    cont += 1
    nota = float(input(f'Digite a {cont}ª nota: '))
    if nota >= 0:
        notas.append(nota)
    elif nota == -1:
        print('Processando...')
        sleep(.5)
        break
    else:
        print('Nota inválida! tente novamente ')
print(f'Quantidade de valores lidos: {len(notas)}\n'
      f'Soma da notas lidas: {sum(notas)}\n'
      f'Média dos valores digitados: {sum(notas) / len(notas):.2f}')
cont_maior_media = cont_menor_sete = 0
for n in notas:
    if n > (sum(notas)/len(notas)):
        cont_maior_media += 1
    if n < 7:
        cont_menor_sete += 1
print(f'Notas acima da média: {cont_maior_media}\n'
      f'Notas abaixo de 7: {cont_menor_sete}\n')
sleep(1)
print('Analise finalizada!')
