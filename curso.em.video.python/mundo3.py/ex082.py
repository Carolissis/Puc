lista = []
par = []
impar = []
r = 's'

while r == 's':
    num = int(input('Digite um número: '))
    lista.append(num)
    r = str(input('Deseja continuar? [S/N] ')).lower().strip()
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

lista.sort()
par.sort()
impar.sort()

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')