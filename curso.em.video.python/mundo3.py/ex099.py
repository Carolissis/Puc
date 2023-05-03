def maior(lista):
    maior = 0 
    for e in lista:
        if e > maior:
            maior = e
    print(f'O maior número dentro da lista {lista} é {maior}')

lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp = str(input('Deseja continuar? [S/N]\nR: ')).strip().lower()[0]
    if resp == 'n':
        break 

maior(lista)