#progressao aritmetica

n = int(input('Digite o número: '))
razao = int (input('Digite a razão: '))
termo = n
count = 1 

while count <=10:
    print('{} ->'.format(termo), end='')
    termo+= razao
    count += 1 
print('FIM')
