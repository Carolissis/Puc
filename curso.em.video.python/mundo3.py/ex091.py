from random import randint 
from time import sleep 
from operator import itemgetter

jogo = {'1º jogador' : randint(1, 6),
        '2º jogador' : randint(1, 6),
        '3º jogador' : randint(1, 6),
        '4º jogador4' : randint(1, 6)} 
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print('='*20)
print('RANKING JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

    #teste