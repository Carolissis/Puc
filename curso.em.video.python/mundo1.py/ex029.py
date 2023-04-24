#multa de velocidade
v= int(input('Qual a velocidade do seu carro? '))
if v <= 80: 
    print( "\033[0;32m"'Tenha um bom dia! Dirija com seguranca!'"\033[0;0m")
else:
    print("\033[1;31m"'MULTADO! Voê escedeu o limite permitido de 80Km/h,') 
    print('você devera pagar uma multa de R${:.2f}'.format(float(v-80)*7), "\033[0;0m")
