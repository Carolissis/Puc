#Conversao de moedas
x= float(input('Quanto de dinheiro voce tem na carteira? R$'))
dol= x/ 5.24
print('Com R${:.2f} você pode comprar US${:.2f}!'.format(x, dol))