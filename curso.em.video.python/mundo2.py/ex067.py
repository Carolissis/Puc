n = 0 

while True:
    n = int(input('Digite um número [negativo parar parar]: '))
    if n < 0:
        break 
    print('-'*15)
    print(f'TABUADA DE {n}')
    print('-'*15)
    for c in range(1,11):
        print(f'{c} X {n} = {n*c}')
    
print('FIM')
