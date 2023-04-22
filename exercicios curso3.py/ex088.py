#mega sena 
from time import sleep
from random import randint

jogo = list()
jogos = list()

print('-'*28)
print(' '*5, 'JOGO NA MEGA SENA')
print('-'*28)

quantjogos = int(input('Quantos jogos você quer que eu sorteie?\nR: '))

for c in range(quantjogos):
    cont = 0
    while True:
       n = randint(1,60) 
       if n not in jogo:
        jogo.append(n)
        cont += 1 
        if cont <= 6:
         jogo.sort()
         jogos.append(jogo[:])
         jogo.clear()  
    # for c in range(0,6):
    #     n = randint(1,60)
    #     jogo.append(n)
    # jogos.append(jogo[:])
    # jogo.clear()

print('\033[33m-='*3,f'SORTEANDO {quantjogos} JOGOS', '=-'*3 , ' \033[m')
for c in range(quantjogos):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)
