#  Criar um programa que efetua a soma de duas matrizes 3x3, sabendo
# que a soma das matrizes 3x3 é uma nova matriz 3x3 onde cada elemento
# é resultado da soma dos elementos das matrizes na mesma posição.

m1  = [[0,0,0], [0,0,0], [0,0,0]]
m2  = [[0,0,0], [0,0,0], [0,0,0]]
m12 = [[0,0,0], [0,0,0], [0,0,0]]
for x in range(3):
    for y in range(3):
        n = int(input(f'Matriz 1 ({x},{y}): '))
        m1[x][y] = n

for x in range(3):
    for y in range(3):
        n = int(input(f'Matriz 2 ({x},{y}): '))
        m2[x][y] = n

for x in range(3):
    for y in range(3):
        m12[x][y] = m1[x][y] + m2[x][y]

print('A soma das matrizes é igual a:')
for c in range(3):
    print(m12[c])