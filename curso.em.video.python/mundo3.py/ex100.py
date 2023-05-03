from random import randint

num = []
def sorteia():
    for c in range(5):
        n = randint(0,20)
        num.append(n)
    print(f'Sorteando 5 valorres da lista: ',end=' ')
    for n in num:
        print(f'{n}',end=', ')
    print('PRONTO!')

def soma():
    soma = 0
    for e in num:
        if e % 2 == 0:
            soma +=e
    print(f'Somando os valores pares da lista {num}, temos {soma}')

sorteia()
soma()
