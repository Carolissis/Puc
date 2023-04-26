lista = []
soma = 0

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Deseja continuar? [S/N]\nR:')).lower().strip()
    if resp in 'n':
        break 

for n in lista:
    soma += n

lista.sort()
print(f'Sua lista é {lista}')
print(f'A média dessee valores é: {soma / len(lista):.2f}')