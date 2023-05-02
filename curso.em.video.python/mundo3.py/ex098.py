from time import sleep

def lin():
    print('-='*15)

def contador(i, f, p):
    lin()
    print(f'Contagem de {i} até {f} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        count = i
        while count <= f:
            print(f'{count} ', end='', flush = True)
            sleep(0.5)
            count += p
        print('FIM')
        lin()
    else:
        count = i
        while count >= f:
            print(f'{count} ', end='', flush = True)
            sleep(0.5)
            count -= p
        print('FIM')
        

#Programa principal
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passos: '))

contador(1, 10, 1)
contador(10, 0, 2)
contador(i, f, p)
