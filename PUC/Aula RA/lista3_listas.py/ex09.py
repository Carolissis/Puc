times = []
pontos = [0, 0, 0, 0]

for t in range(4):
    time = str(input(f'{t+1}° time: ')).upper()
    times.append(time)

for i, t1 in enumerate(times):
    for l, t2 in enumerate(times):
        if i != l:
            print(f'JOGO: {t1} VS {t2}')
            print('RESULTADO')
            op = int(input(f'[1]EMPATE\n[2]{t1} VENCEU\n[3]{t2} VENCEU\nR: '))
            if op == 1:
                pontos[i] += 1
                pontos[l] += 1 
            elif op == 2:
                pontos[i] += 3 
            elif op == 3:
                pontos[l] += 3

for c in range(4):
        print(f'O time {times[c]} fez {pontos[c]} pontos')          