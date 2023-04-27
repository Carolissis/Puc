vetor = []
for c in range(10):
    num = int(input(f'Digite o {c+1} º valor: '))
    vetor.append(num)
vetor.sort(reverse= True)
print(vetor)