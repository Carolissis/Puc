print('\033[35m' ,"="*5,'Escolha uma forma de pagamento','='*5 , '\033[m')
preco = float(input('Qual o valor do prouto? R$ '))
print('Qual a forma de pagamentp?')
print('[1] à vista dinheiro/cheque (10% de desconto)')
print('[2] à vista no cartão (5% de desconto)')
print('[3] em até 2x no cartão (preço normal)')
print('[4] 3x ou mais no cartao (20% de juros)')
opcao = (int(input('R: ')))

if opcao == 1:
    print('O valor total será de R${:.2f}'.format(preco*0.9))
elif opcao == 2:
    print('O valor total será de R${:.2f}'.format(preco*0.95))
elif opcao == 3:
    print('O valor a pagar será de R${:.2f}'.format(preco))
else:
     print('Em quantas parcelas?')
     parc = int(input('R: '))
     print('O valor total será de R${:.2f}'.format(preco+(preco*0.20*parc)))
