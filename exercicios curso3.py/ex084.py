# Perguntar os nomes e peso, falar quantas pessoas foram cadastradas 
# uma lista da/das pessoas mais pesados e peso
# uma lista da/das pessoas mais leves e peso

r = 's'
np = list()
geral = list()
pmai = pmen = 0 

while r == 's':
    np.append(str(input('Nome: ')))
    np.append(float(input('Peso: ')))
    if len(geral) == 0:
        pmai = pmen = np[1]
    else:
        if np[1] > pmai:
            pmai = np[1]
        if np[1] < pmen:
            pmen = np[1]
    geral.append(geral[:])
    r = str(input('Deseja continuar? [S/N] '))

print(f'{len(geral)} pessoas foram cadastradas.')
print(f'O maior peso foi de {pmai:.2f}Kg.', end='')
for p in geral:
    if p[1] == pmai:
        print(f'[{p[0]}]', end='')    
print(f'O menor peso foi de {pmen:.2f}Kg.', end= '')
for p in geral:
    if p[1] == pmen:
        print(f'[{p[0]}]', end='')