massa_inicial = float(input("Digite a massa inicial (em gramas): "))
massa_atual = massa_inicial
tempo = 0

while massa_atual >= 0.5:
    massa_atual /= 2
    tempo += 50

print("Massa final: {:.2f} gramas".format(massa_atual))
print("Tempo necessário: {} segundos".format(tempo))
