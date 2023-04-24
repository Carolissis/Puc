
print('-=-'*14)
print('ANALISANDO O TRIANGULO')
print('-=-'*14)
a= float(input('Lado 1: '))
b= float(input('Lado 2: '))
c= float(input('Lado 3: '))
if a < b+c and b< a+c and c < b+a:
    print('Seu triandulo é possivel')
else: 
    print('Não é possivel criar esse triangulo')