preco= float(input('\033[36mQual o valor do produto?\033[m \n R%: '))
forma= int(input('\033[36mEscolha a forma de pagamento:\033[m \n [1] À vista em dinheiro ou cheque (10%)\n [2] À vista no cartão (15%)\n [3] Em duas vezes \n [4] Em tres vezes (juros de 10%) \n R:'))
if forma == 1:
    print('O valor a pagar será R${:.2f}'.format(preco*0.90))
elif forma == 2:
    print('O valor a pagar será R${:.2f}'.format(preco*0.85))
elif forma == 3:
    print('O valor a pagar será R${:.2f}'.format(preco))
else:
    print('O valor a pagar será R${:.2f}'.format(preco*1.1))