lista =[]

while True:
    n = int(input('Digite um numero: '))
    if n not in lista: 
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Numero ja esta na lista, deseja continuar? [S/N]')
        r = str(input('R: '))
        if r in 'Nn':
            break 
lista.sort()
print(lista)