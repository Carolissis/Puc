# preco do produto com desconto (5%)
x= float(input("Qual é o preco do produto?  R$"))
desc= float(x- (x*5/100))
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(x,desc))
