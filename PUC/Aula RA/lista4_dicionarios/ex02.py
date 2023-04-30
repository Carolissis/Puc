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

ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

imprimir_unidades(unidades)

valor = obter_valor()
unidade_origem = obter_unidade_origem()
unidade_destino = obter_unidade_destino()

if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
    print("Unidade(s) inválida(s). Certifique-se de usar as abreviações corretas.")
else:
    valor_convertido = converter_unidades(valor, unidade_origem, unidade_destino, ano_luz)
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido} {unidade_destino}")
