# Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
# para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
# final e o tempo calculado em segundos.

massa_inicial = float(input("Digite a massa inicial (em gramas): "))
massa_atual = massa_inicial
tempo = 0

while massa_atual >= 0.5:
    massa_atual /= 2
    tempo += 50

print("Massa final: {:.2f} gramas".format(massa_atual))
print("Tempo necessário: {} segundos".format(tempo))
