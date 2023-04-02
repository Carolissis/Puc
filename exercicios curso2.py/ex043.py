print('-=-'*5)
print('Calculando IMC')
print('-=-'*5)
p= float(input('Qual é o seu peso? '))
h= float(input('Qual é a sua altura? '))
imc= p/(h**2)
if imc <= 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Peso normal')
elif imc > 25 and imc <= 30:
    print('Acima do peso')
elif imc > 30 and imc <=40:
    print('Obesidade')
else:
    print("\033[31m"'Obesidade mórbida'"\033[m")