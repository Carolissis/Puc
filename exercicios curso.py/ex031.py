
d= int(input('Qual a distância da sua viagem?: '))
"""if d <= 200:
    print('O valor da sua viagem será R${:.2f}'.format(float(d*0.5)))
else:
    print('O valor da sua viagem será R${:.2f}'.format(float(d*0.45)))"""
preco= d*0.5 if d <= 200 else d*0.45
print('O valor da sua viagem será R${:.2f}'.format(preco))