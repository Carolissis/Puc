print('Qual é o seu destino? ')
print('Região Norte [1]')
print('Região Nordeste [2]')
print('Região Centro Oeste [3]')
print('Região Sul [4]')
reg = int(input('R: '))
print('So ida [1] \nIda e volta [2]')
ida = int(input('R: '))

if reg == 1:
    if ida == 1:
        print('O valor da viagem será R$500.00')
    else:
        print('O valor da viagem será R$900.00')
if reg == 2:
    if ida == 1:
        print('O valor da viagem será R$350.00')
    else:
        print('O valor da viagem será R$650.00')
if reg == 3:
    if ida == 1:
        print('O valor da viagem será R$350.00')
    else:
        print('O valor da viagem será R$600.00')
if reg == 4:
     if ida == 1:
        print('O valor da viagem será R$300.00')
     else:
        print('O valor da viagem será R$550.00')