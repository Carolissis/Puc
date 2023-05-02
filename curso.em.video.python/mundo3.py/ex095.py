jogador = {}
jogadores = []
total = 0
gols = []
while True:
    jogador.clear()
    total = 0
    gols = []
    jogador['Nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for p in range(partidas):
        gols.append(int(input(f'Quantos gols na {p+1}º partida: ')))
    for g in gols:
        total += g
    jogador['Gols'] = gols
    jogador['Total'] = total
    jogadores.append(jogador.copy())
    perg = str(input('Deseja continuar? [S/N]: ')).lower()
    if perg == 'n':
        break

print('-='*20)
print(f'{"cod nome":<12}{"gols":>8}{"total":>15}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i} {v["Nome"]:<10}{str(v["Gols"]):>10} {v["Total"]:>15}')
print('-'*40)

while True:
    print('Mostrar dados de qual jogador? (999 para parar)')
    resp = int(input('R: '))
    if resp == 999:
        break
    else:
        p = 1
        print(f'Levantamento do jogador {jogadores[resp]["Nome"]}')
        for v in jogadores[resp]['Gols']:
            print(f'No jogo {p} fez {v} gols.')
            p +=1
        