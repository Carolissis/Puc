# Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
# e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
# um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
# tempo necessário para que a população do país A ultrapasse a população do país B.

populacao_a = 5000000
populacao_b = 7000000
taxa_natalidade_a = 0.03
taxa_natalidade_b = 0.02
anos = 0

while populacao_a <= populacao_b:
    populacao_a *= 1 + taxa_natalidade_a
    populacao_b *= 1 + taxa_natalidade_b
    anos += 1

print("A população do país A ultrapassará a população do país B em {} anos.".format(anos))
