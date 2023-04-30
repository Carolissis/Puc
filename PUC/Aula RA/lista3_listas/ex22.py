# Lista de defeitos
defeitos = [
    "necessita da esfera",
    "necessita de limpeza",
    "necessita troca do cabo ou conector",
    "quebrado ou inutilizado"
]

# Inicializa uma lista para armazenar a contagem de defeitos
contagem_defeitos = [0] * len(defeitos)

# Inicializa a quantidade total de mouses testados
total_mouses = 0

while True:
    id_mouse = int(input("Digite o número de identificação do mouse (0 para encerrar): "))
    if id_mouse == 0:
        break

    print("Tipos de defeito:")
    for i, defeito in enumerate(defeitos, start=1):
        print(f"{i} - {defeito}")
    
    tipo_defeito = int(input("Digite o número correspondente ao tipo de defeito: "))
    while tipo_defeito < 1 or tipo_defeito > len(defeitos):
        tipo_defeito = int(input("Número inválido. Digite novamente o número correspondente ao tipo de defeito: "))
    
    contagem_defeitos[tipo_defeito - 1] += 1
    total_mouses += 1

# Exibe o relatório
print("\nRelatório:")
print(f"Quantidade de mouses: {total_mouses}")
print("Situação " + " " * 6 + "Quantidade" + " " * 4 + "Percentual")
for i, defeito in enumerate(defeitos, start=1):
    percentual = (contagem_defeitos[i - 1] / total_mouses) * 100
    print(f"{i} - {defeito:35} {contagem_defeitos[i - 1]:10} {percentual:5.1f}%")
