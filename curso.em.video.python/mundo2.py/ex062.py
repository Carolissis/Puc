print('PROGRAMADOR DE PA')
print('-='*9)

n = int(input('Digite o número: '))
razao = int (input('Digite a razão: '))
termo = n
count = 1 
total = 0 
mais = 10 

while mais != 0 :
    total += mais 
    while count <= total :
        print('{} ->'.format(termo), end='')
        termo+= razao
        count += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))