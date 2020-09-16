"""
 08) Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
  Imprima a idade e a altura na ordem inversa a ordem lida.
"""
idade = list()
altura = list()
for n in range(0, 5):
    print(f'{n+1}ª Pessoa - >')
    while True:
        i = input('Idade: ')
        if i.isnumeric() and (1 <= int(i) <= 120):
            idade.append(int(i))
            break
        else:
            print('Idade precisa ser um número entre 1 e 120. Tenten novamente.')
    while True:
        a = input('Altura: ')
        if a.isnumeric() and (.60 < float(a) < 350.0):
            altura.append(float(a))
            break
        else:
            print('Altura precisa ser um número entre 0.60cm e 350.0cm. Tente novamente.')
for pesoa in range(4, -1, -1):
    print(f'{pesoa+1}ª Pessoa tem {idade[pesoa]} anos de idade e {altura[pesoa] / 100:.2f}m de altura!')