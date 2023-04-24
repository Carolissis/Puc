# pedir 7 numeors para o usuario 
# colocar em uma lista unica 
# separar em lista de pares e impares em ordem crescente 

pares = []
impares = []
geral = list()

for c in range(0,7):
    num = int(input('Digite um valor: '))
    geral.append(num)
    if num % 2 == 0:
        pares.append(geral[c:])
    if num % 2 == 1:
        impares.append(geral[c:])
geral.sort()
pares.sort()
impares.sort()

print(f'Os numeros digitados foram: {geral}')
print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
