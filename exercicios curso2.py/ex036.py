#aprovando emprestimo 
c= int(input('Qual o valor da casa?' ))
s= int(input('Qual o salário do comprador? '))
a= int(input('Em quantos anos o financiamento? '))
prestacao = c/ (a*12)
min = s * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestacao devará ser de {}.'.format(c,a,prestacao))
if prestacao <= min:
    print('Emprestimo pode ser CONCEDIDO!!')
else:
    print('Emprestimo NEGADO!!')
