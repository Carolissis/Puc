# Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
# porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.

from time import sleep

print('-'*20)
print('Pedra/Papel/Tesoura')
print('-'*20)

sleep(2)

p1 = 0
p2 = 0 
for c in range(1, 7):
    print('[1]PEDRA\n[2]PAPEL\n[3]TESOURA')
    print('Jogador 1 faça sua escola: ')
    j1 = int(input(': '))
    print('Jogador 2 faça sua escola: ')
    j2 = int(input(': '))

    if j1==1:
        if j2==1:
            p1+=1
            p2+=1
        elif j2 == 2:
            p1+=0
            p2+=2
        else:
            p1+=2
            p2+=0

    if j1==2:
        if j2==2:
            p1+=1
            p2+=1
        elif j2 == 3:
            p1+=0
            p2+=2
        else:
            p1+=2
            p2+=0

    if j1==3:
            if j2==3:
                p1+=1
                p2+=1
            elif j2 == 1:
                p1+=0
                p2+=2
            else:
                p1+=2
                p2+=0
    if p1 >= 7:
        print('Jogador 1 vneceu com {} pontos e o jogador 2 ficou com {} pontos e foram {} partidas'.format(p1, p2, c))
    elif p2 >= 7:
        print('Jogador 2 venceu com {} pontos e o jogador 1 ficou com {} pontos e foram {} partidas'.format(p2, p1, c))
        break
        