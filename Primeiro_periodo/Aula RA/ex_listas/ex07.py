m =[[0,0,0],
    [0,0,0],
    [0,0,0]]
num = []

for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para ({l+1},{c+1}): '))
        num.append(n)

num.sort(reverse= True)
for i, n in enumerate(num):
    l = i // 3
    c = i % 3  
    m[l][c]= n   
print(m)
