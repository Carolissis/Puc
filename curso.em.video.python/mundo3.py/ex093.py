jogador = {}
total = 0
gols = []
jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for p in range(partidas):
    num = int(input(f'Quantos gols na {p+1}º partida: '))
    gols.append(num)
    total += num 
jogador['Gols'] = gols 
jogador['Total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for p in range(partidas):
    print(f'{"=>":>4} Na partida {p+1}, fez {jogador["Gols"][p]} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')