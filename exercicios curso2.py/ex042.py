print('-'*23)
print('Analisando triangulos')
print('-'*23)

a = (int(input('Primeiro segmento: ')))
b = (int(input('Segundo segmento: ')))
c = (int(input('Terceiro segmento: ')))
if a < b + c and b < a + c and c < a + b:
    print('O triangulo é possivel: ')
    if a == b == c:
        print('O triangulo é EQUILATERO')
    elif a != b != c !=a: 
        print('O triangulo é ESCALENO')
    else: 
        print('O triangulo é ISOCELES')
else:
    print('O triangulo não pode ser formado com esses segmentos ')
