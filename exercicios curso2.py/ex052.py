#Numeros primos

tot = 0 
num = int(input('Digite um número: '))
for c in range( 1, num+ 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
    print('\033[m', end='')
print('\nO  numero {} foi divisivel {} vezes'.format(c,tot ))
if tot == 2:
    print('Seu numero é primo')
else:
    print('O numero {} não é primo'.format(num))