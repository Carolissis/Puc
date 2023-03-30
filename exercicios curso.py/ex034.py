
s= int(input('Qual é o seu salário? '))
if s <= 1250:
    a= s*1.15
else:
    a=s*1.1

print('O seu salário vai de R${:.2f} para R${:.2f}'.format(s,a))