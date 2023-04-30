import random

def lancar_dado():
    return random.randint(1, 6)

# Inicializa um vetor de contadores para os valores dos dados (1-6)
contadores = [0] * 6

# Lança o dado 100 vezes e armazena os resultados no vetor de contadores
for _ in range(100):
    resultado = lancar_dado()
    contadores[resultado - 1] += 1

# Mostra quantas vezes cada valor foi conseguido
for i, contador in enumerate(contadores, start=1):
    print(f"O valor {i} foi conseguido {contador} vezes.")
