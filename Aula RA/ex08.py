dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))
hora = int(input('Hora: '))
min = int(input('Minuto: '))
seg = int(input('Segundo: '))

print("Data e hora informada: {}/{}/{} {}:{}:{}".format(dia, mes, ano, hora, min, seg ))

print('Qual informção você deseja acrescetar?')
print('Dia [1]')
print('Mes [2]')
print('Ano [3]')
print('Hora [4]')
print('Minuto [5]')
print('Segundo [6]')
opcao = int(input('R: '))

if opcao == 1: 
    dias = int(input('Quantos dias deseja acrescentar? '))
    while dias > 0: 
        if 