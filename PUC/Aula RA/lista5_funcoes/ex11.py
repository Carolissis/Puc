

data = []
entrada = input('Digite a data (DD/MM/AAAA): ')
data.extend(entrada.split('/'))
dia = data[0]
mes = data[1]
ano = data[2]
print(dia,mes,ano)