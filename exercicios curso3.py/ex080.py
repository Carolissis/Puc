lista = []
maior = 0
menor = 0

for c in range(1, 6):
    num = int(input(f'Digite o {c}º número: '))
    
    if c == 0:
        menor = maior = num
        lista.insert(0, num)

    else:
        if num > maior:
            lista.insert(-1, num)
        if num < menor:
            lista.insert(0, num)
print(lista)