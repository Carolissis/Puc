#Aluguel de Carro
x= int(input('Quantos dias voce alugou o carro? '))
y= float(input('Quantos km você andou? '))
total= (x*60) + (y*0.15)
print('o total a pagar é de R${:.2f}'.format(total))