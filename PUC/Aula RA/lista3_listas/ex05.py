inte = []
par = []
imp = []
for c in range(20):
    num = int(input(f'{c+1}º número: '))
    inte.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
inte.sort()
par.sort()
imp.sort()
print(f'Os números digitados fora: {inte}\n    Pares: {par}\n   Impares: {imp}')