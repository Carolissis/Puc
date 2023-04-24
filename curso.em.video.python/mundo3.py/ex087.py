m = [[0,0,0], [0,0,0], [0,0,0]]
spar = scol = mai = 0

for l in range(0,3):
    for c in range(0,3):
        lista = list()
        m [l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        lista.append(m)
print('='*38)

# matriz e a soma dos numeros pares 
for l in range(0,3):
    for c in range(0,3):
        print(f'[{m[l][c]:^5}]', end=" ")
        if m[l][c] % 2 == 0:
            spar += m[l][c]
    print()
# soma da coluna 3
for c in range(0,3):
    scol += m[c][2]
# maior num da linha 1 
for c in range(0,3):
    mai = m[0][0]
    if c > 0:
        if m[0][c] > mai:
            mai = m[0][c]     

print(f'A soma dos números pares é: {spar}')
print(f'A soma da terceira coluna é: {scol}')
print(f'O maior número da primeira linha é: {mai}')
