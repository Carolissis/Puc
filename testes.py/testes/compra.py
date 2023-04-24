prod= input('Digite o nome do produto: ')
value= float(input('Digite o valor do produto: '))
quant= float(input('Digite a quantidade do produto: '))
preco= value*quant
print(f'O valor totalda compra foi R${preco: .2f}')
y= float(preco) * 0.15 
x= preco - y 
print(f'Se o pagamento for a vista, o total fica R${x: .2f}')