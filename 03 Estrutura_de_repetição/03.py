"""
 03) Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
while True:
    nome = str(input('Nome: '))
    if len(nome) < 3:
        print('O nome deve ter mais de 3 caractéres! tente novamente!!')
    else:
        break
while True:
    idade = int(input('Idade: '))
    if 0 < idade <= 150:
        break
    else:
        print('Idade inválida')
while True:
    salario = float(input('Salário: '))
    if salario < 0:
        print('valor iválido informado, tente novamente!!')
    else:
        break
while True:
    sexo = str(input('Sexo: [m/f] ')).strip().upper()[0]
    if sexo not in 'FM':
        print('valor inválido informado, tente novamente!!')
    else:
        break
while True:
    print(f"{'Estado Civil:':^30}\n{'-'*30}\n"
          f"(S) Solteiro(a)\n"
          f"(C) Casado(a)\n"
          f"(V) Viuvo(a)\n"
          f"(D) Divorciado(a)\n{'-'*30}")
    civil = str(input('Estado civil: ')).strip().upper()[0]
    if civil not in 'SCVD':
        print('Valor informado inválido, tente novamente!')
    else:
        break
print(f"{'='*30}\n{f'Cadastro de {nome} realizado com sucesso!!':^30}\n{'='*30}")
