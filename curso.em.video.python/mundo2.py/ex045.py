#Pedra papel tesoura 

from random import randint
itens= ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2) #computador

print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
p = int(input('R: ')) #pessoa

if p == 0:
    if c == 0:
        print('\033[33mEMPATE, o computador escolheu {}\033[m'.format(itens[c]))
    elif c == 1:
        print('\033[31mVocê PERDEU, o computador jogou {}\033[m'.format(itens[c]))
    else:
        print('\033[32mVocê VENCEU, o computador jogou {}\033[m'.format(itens[c]))
if p == 1: 
    if c == 0:
        print('\033[32mVocê VENCEU, o computador jogou {}\033[m'.format(itens[c]))
    elif c == 1:
        print('\033[33mEMPATE, o computador escolheu {}\033[m'.format(itens[c]))
    else:
        print('\033[31mVocê PERDEU, o computador jogou {}\033[m'.format(itens[c]))
if p == 2:
    if c == 0:
        print('\033[31mVocê PERDEU, o computador jogou {}\033[m'.format(itens[c]))
    elif c == 1:
        print('\033[32mVocê VENCEU, o computador jogou {}\033[m'.format(itens[c]))
    else:
        print('\033[33mEMPATE, o computador escolheu {}\033[m'.format(itens[c]))