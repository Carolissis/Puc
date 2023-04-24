#progressão aritmetca

print('='*21)
print(' 10 TERMOS DE UMA PA ')
print('='*21)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = p + (10-1)*r


for c in range(p, dec + r , r):
    print(c, end=" ")