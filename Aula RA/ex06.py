a = int(input('Valor A: '))
b= int(input('Valor B: '))
c = int(input('Valor C: '))
delta = b**2- (4*a*c)
r1 = (-b + delta**1/2) / (2*a)
r2 = (-b - delta**1/2) / (2*a)

print('Os resultados são {:.2f} e {:.2f}'.format(r1, r2))