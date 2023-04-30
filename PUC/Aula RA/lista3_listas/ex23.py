def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)


def calcular_percentual(valor, total):
    return (valor / total) * 100


# Lê o arquivo de entrada e armazena os dados em uma lista de tuplas
with open("usuarios.txt", "r") as arquivo:
    usuarios = [tuple(linha.strip().split()) for linha in arquivo]

# Converte o espaço ocupado em disco de bytes para megabytes e calcula o total
espacos_mb = [bytes_para_mb(int(espaco)) for _, espaco in usuarios]
total_mb = sum(espacos_mb)

# Gera o relatório
with open("relatório.txt", "w") as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 70 + "\n")
    relatorio.write("Nr. Usuário" + " " * 5 + "Espaço utilizado" + " " * 5 + "% do uso\n")

    for i, (usuario, espaco) in enumerate(usuarios, start=1):
        espaco_mb = espacos_mb[i - 1]
        percentual = calcular_percentual(espaco_mb, total_mb)
        relatorio.write(f"{i} {usuario:<15} {espaco_mb:10.2f} MB {percentual:10.2f}%\n")

    relatorio.write("\n")
    relatorio.write(f"Espaço total ocupado: {total_mb:.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {total_mb / len(usuarios):.2f} MB\n")
