Area_doacao = True
doa = True
pag = True
lista = [1, 2 ,3]
while Area_doacao ==  True:
    while doa == True:
        doacao = int(input('Digite o valor que deseja doar: '))
        if doacao <= 0:
            print('Valor invalido')
        else: 
            doa = False
    while pag == True:
        print('Forma de pagamento:\n[1] Cartão de crédito\n[2] Boleto\n[3] PIX\n')
        pagamento = int(input('R: '))
        if pagamento not in lista:
            print('Forma de pagamento inválida')
        else: 
            print('Obrigada por ajudar a Amazonia a ficar cada vez mais verde :)')
            pag = False
            Area_doacao = False
