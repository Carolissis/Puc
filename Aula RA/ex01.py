sex= input('Qual seu sexo? ').lower()
h= float(input('Qual a sua altura? '))
if sex == "masculino":
    print('Seu peso ideal é {:.2f}'.format((72.7*h)-58))
else:
    print('Seu peso ideal é {:.2f}'.format((62.1*h)-44.7))

