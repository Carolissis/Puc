import uteis02
ano_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

uteis02.imprimir_unidades(unidades)

valor = uteis02.obter_valor()
unidade_origem = uteis02.obter_unidade_origem()
unidade_destino = uteis02.obter_unidade_destino()

if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
    print("Unidade(s) inválida(s). Certifique-se de usar as abreviações corretas.")
else:
    valor_convertido = uteis02.converter_unidades(valor, unidade_origem, unidade_destino, ano_luz)
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido} {unidade_destino}")
