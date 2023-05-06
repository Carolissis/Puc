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