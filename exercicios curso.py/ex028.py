#jogo advinhacao 
import random
from time import sleep
print("\033[1;36m""-"*55,"\033[0;0m")
print("\033[1;34m"'Vou pensar em um número entre 0 e 5. Tente advinhar...'"\033[0;0m")
print("\033[1;36m""-"*55,"\033[0;0m")
num= int(input('Digite o seu numero: '))
lista= [0,1,2,3,4,5]
x= random.choice(lista)
print('PROCESSANDO...')
sleep(2)
if num==x:
    print("\033[0;32m"'PARABENS! VOCÊ ACERTOU, O NUMERO CORRETO ERA {}'.format(x),"\033[0;0m")
else:
    print( "\033[1;31m"'TENTE NOVAMENTE, MEU NUMERO ERA {}'.format(x),"\033[0;0m")

"""from random import randint
computador= radint(0,5) """