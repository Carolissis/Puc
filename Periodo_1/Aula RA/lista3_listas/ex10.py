#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
#valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

pri = []
seg = []
for e in range(20):
    if e < 10:
        num = int(input(f'{e+1}º valor do primeiro vetor: '))
        pri.append(num)
    else:
        num = int(input(f'{e-9}º valor do segundo vetor: '))
        seg.append(num)

for i, v in enumerate(pri):
    print(f'{v},{seg[i]},', end='')