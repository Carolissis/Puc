sexo = str(input('Informe seu sexo: \n[M/F]\nR: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, infrome seu sexo: \n[M/F]\nR: ')).strip().upper()[0]
if sexo in 'M':
    sexo = 'Masculino'
else:
    sexo = 'Femenino'
print('Sexo {} registrado com sucesso'.format(sexo))

