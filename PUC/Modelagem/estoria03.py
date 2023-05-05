Produtos_biodegradaveis = True
prod = True
pag = True
prod_prec =['Papel Semente','Talheres Bio' ,
            'Canudo','Lápis Semente', 'Escova de Bamboo']
lista = [1,2,3,4,5]

while Produtos_biodegradaveis == True:
    while prod == True:
        print('Produtos:')
        i = 1
        for p in prod_prec:
            print(f'{i} {p}')
            i += 1
        opcao = int(input('Produto: '))
        if opcao not in lista:
            print('Opção invalida')
        else:
            prod = False
    while pag == True:
        print('Forma de pagamento:\n[1] Cartão de crédito\n[2] Boleto\n[3] PIX\n')
        pagamento = int(input('R: '))
        if pagamento not in lista:
            print('Forma de pagamento inválida')
        else: 
            print('Obrigada por ajudar a Amazonia a ficar cada vez mais verde :)')
            pag = False
            Produtos_biodegradaveis = False

    
