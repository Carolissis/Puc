lista = []
maior = 0
menor = 0

for c in range(1, 6):
    num = int(input(f'Digite o {c}º número: '))
    
    if c == 1 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos , num)
                print(f'Adicionado na posicao {pos} da lista...')
                break 
            pos +=1
print(lista)