#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada

pri = []
seg = []
ter = []
for e in range(30):
    if e < 10:
        num = int(input(f'{e+1}º valor do primeiro vetor: '))
        pri.append(num)
    elif 10<= e < 20:
        num = int(input(f'{e-9}º valor do segundo vetor: '))
        seg.append(num)
    else:
        num = int(input(f'{e-19}º valor do terceiro vetor: '))
        ter.append(num)

for i, v in enumerate(pri):
    print(f'{v},{seg[i]},{ter[i]},', end='')