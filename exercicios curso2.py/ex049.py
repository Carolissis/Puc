#tabuada 
num = int(input('Digite um número para ver sua tabuada: '))
for n in range(1,11):
    print('{} X {:2} = {}'.format(num, n, num*n))