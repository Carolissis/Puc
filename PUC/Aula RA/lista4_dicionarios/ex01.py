def imprimir_cardapio(cardapio):
    print("Cardápio do Restaurante Boca Feliz:")
    for i, item in enumerate(cardapio, start=1):
        print(f"{i}. {item}")
    print()

def obter_pedido():
    return input("Escolha o número do produto que deseja pedir (0 para sair): ")

def verificar_disponibilidade(produto, cardapio, estoque):
    ingredientes = cardapio[produto]
    faltando = []
    for ingrediente in ingredientes:
        if ingrediente not in estoque or estoque[ingrediente] < 1:
            faltando.append(ingrediente)
    return faltando

def produzir_produto(produto, cardapio, estoque):
    ingredientes = cardapio[produto]
    for ingrediente in ingredientes:
        estoque[ingrediente] -= 1

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
    imprimir_cardapio(cardapio_numerado)
    pedido = obter_pedido()

    if pedido == "0":
        break

    try:
        produto = cardapio_numerado[int(pedido) - 1]
    except (IndexError, ValueError):
        print("Número inválido, tente novamente.")
        continue

    ingredientes_faltando = verificar_disponibilidade(produto, cardapio, estoque)

    if ingredientes_faltando:
        for ingrediente in ingredientes_faltando:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        produzir_produto(produto, cardapio, estoque)
        print(f"Um {produto} saindo no capricho!!!")

print("Obrigado por utilizar o Restaurante Boca Feliz!")
