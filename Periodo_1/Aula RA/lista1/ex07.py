print('Quando é o seu aniversário? ')
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

abre = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
comp = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

print('Escolha uma opção: ')
print('Normal ex: 10/10/2010 [1]')
print('Abreviada ex 10/out/2010 [2]')
print('Completa ex: 10 de outubro de 2010 [3]')
opcao = int(input('R: '))

if opcao == 1:
    print('{}/{}/{}'.format(dia, mes, ano))
if opcao == 2:
    print('{}/{}/{}'.format(dia, abre[mes-1], ano))
if opcao == 3:
    print('{} de {} de {}'.format(dia, comp[mes-1], ano))
