Produtos_plantio = True
prod = True
pag = True
prod_prec =['Semente de Girasol','Pá de jardineiro' ,
            'Luvas','Adubo Orgânico', 'Semente de Canabis medicinal']
lista = [1,2,3,4,5]

while Produtos_plantio == True:
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
            Produtos_plantio = False

    
