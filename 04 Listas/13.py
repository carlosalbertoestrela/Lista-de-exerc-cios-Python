"""
 13) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
 Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
 e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp_meses = list()
for mes in range(len(meses)):
    while True:
        temperatura = input(f'Digite a temperatura média do mês {mes+1} - {meses[mes]}: ')
        if temperatura.isnumeric():
            temp_meses.append(float(temperatura))
            break
        else:
            print('A temperatura precisa ser um número! Tente novamente.')
media_temp = sum(temp_meses) / len(temp_meses)
print(f'Os meses acima {media_temp:.1f}º que é a média de temperatura anual são: ')
for t in range(len(temp_meses)):
    if temp_meses[t] > media_temp:
        print(f'{t+1} - {meses[t]} = {temp_meses[t]:.1f}º')
