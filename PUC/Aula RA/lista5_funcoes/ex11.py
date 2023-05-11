meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def data_extensa(a, b, c):
    mese = meses[b-1]
    return f'{a} de {mese} de {c}'

data = []
entrada = input('Digite a data (DD/MM/AAAA): ')
data.extend(entrada.split('/'))
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

print(data_extensa(dia,mes,ano))