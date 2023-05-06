def imprimir_unidades(unidades):
    print("Unidades de Conversão:")
    for unidade in unidades:
        print(unidade)
    print()

def obter_valor():
    return float(input("Valor a ser convertido: "))

def obter_unidade_origem():
    return input("Converter de: ").lower()

def obter_unidade_destino():
    return input("Converter para: ").lower()

def converter_unidades(valor, unidade_origem, unidade_destino, anos_luz):
    valor_em_anos_luz = valor * anos_luz[unidade_origem]
    valor_convertido = valor_em_anos_luz / anos_luz[unidade_destino]
    return valor_convertido