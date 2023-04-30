def calcular_salario(vendas_brutas):
    salario_base = 200
    comissao = 0.09
    return salario_base + (vendas_brutas * comissao)

def calcular_posicao(salario):
    if salario < 1000:
        return (salario - 200) // 100
    else:
        return 8

# Exemplo de vendas brutas dos vendedores
vendas_brutas_vendedores = [3000, 4500, 1200, 6000, 800, 9500, 6700, 2000, 8900, 10000]

# Inicializa a lista de contadores com 9 elementos (um para cada intervalo de salário)
contadores = [0] * 9

# Para cada vendedor, calcula o salário e incrementa o contador correspondente
for vendas_brutas in vendas_brutas_vendedores:
    salario = calcular_salario(vendas_brutas)
    posicao = calcular_posicao(salario)
    contadores[posicao] += 1

# Exibe a quantidade de vendedores em cada intervalo de salário
print("Vendedores por intervalo de salário:")
print("a. $200 - $299:  ", contadores[0])
print("b. $300 - $399:  ", contadores[1])
print("c. $400 - $499:  ", contadores[2])
print("d. $500 - $599:  ", contadores[3])
print("e. $600 - $699:  ", contadores[4])
print("f. $700 - $799:  ", contadores[5])
print("g. $800 - $899:  ", contadores[6])
print("h. $900 - $999:  ", contadores[7])
print("i. $1000 em diante: ", contadores[8])
