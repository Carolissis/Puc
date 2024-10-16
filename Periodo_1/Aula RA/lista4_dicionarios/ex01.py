import uteis01

estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

cardapio_numerado = list(cardapio.keys())

while True:
    uteis01.imprimir_cardapio(cardapio_numerado)
    pedido = uteis01.obter_pedido()

    if pedido == "0":
        break

    try:
        produto = cardapio_numerado[int(pedido) - 1]
    except (IndexError, ValueError):
        print("Número inválido, tente novamente.")
        continue

    ingredientes_faltando = uteis01.verificar_disponibilidade(produto, cardapio, estoque)

    if ingredientes_faltando:
        for ingrediente in ingredientes_faltando:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        uteis01.produzir_produto(produto, cardapio, estoque)
        print(f"Um {produto} saindo no capricho!!!")

print("Obrigado por utilizar o Restaurante Boca Feliz!")
