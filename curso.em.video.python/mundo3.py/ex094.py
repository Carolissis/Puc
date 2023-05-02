# Exercício Python 094: Crie um programa que leia nome, sexo e idade de 
# várias pessoas, guardando os dados de cada pessoa em um dicionário e 
# todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média
pessoa = dict()
galera = list()
cont = 0
mul = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] == 'F':
            mul.append(pessoa['nome'])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    cont += 1
    while True:
        perg = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if perg in 'SN':
            break
        print('ERRO! Por favor, digite S ou N')
    if perg == 'N':
        break

print(f'A) {cont} pessoas foram cadastradas')
soma = 0
for i, v in enumerate(galera):
    soma += galera[i]['idade']
media = soma / cont
print(f'B) A média de idade é {media:.0f}')
if len(mul) == 0:
    print('C) Nenhuma mulher foi cadastrada.')
else:
    print(f'C) As Mulheres cadastradas foram {mul}')
print('D) Lista de pessoas que estão acima da média')
for i,v in enumerate(galera):
    if galera[i]['idade'] > media:
        print(f'    Nome: {galera[i]["nome"]}; Sexo: {galera[i]["sexo"]}; Idade = {galera[i]["idade"]}')