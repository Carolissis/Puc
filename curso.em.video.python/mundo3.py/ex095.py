jogador = {}
jogadores = []
total = 0
gols = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for p in range(partidas):
        jogador['Gols'] = int(input(f'Quantos gols na {p+1}º partida: '))
        total += jogador['Gols'] 
    jogador['Total'] = total
    jogadores.append(jogador.copy())
