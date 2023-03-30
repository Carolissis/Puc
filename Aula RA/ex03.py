from random import randint

print('-'*20)
print('\033[35m''Jogo par ou impar''\033[m')
print('-'*20)

print('Jogador vs Jogador [1] \nJogador vcs Computaodr [2]')
choise = int(input('R: '))

if choise == 1:
    print('Jogador 1  quer ser [1] par ou [2] impar?')
    j1= int(input('R:'))
    x= input('Escolha um numero Jogador 1 \n R:')
    y=input('Escolha um numero Jogador 2 \n R: ')
    if j1 == 1 and (x+y)%2 == 0:
        print ('\033[32m''Jogador 1 venceu!!''\033[m')
    elif j1 == 1 and (x+y)%2 == 1:
        print('\033[32m''Jogador 2 venvceu!!''\033m')
    elif j1 == 2 and (x+y)%2 == 0:
        print('\033[32m''Jogador 2 venvceu!!''\033m')
    else:
        print ('\033[32m''Jogador 1 venceu!!''\033[m')

if choise == 2: 
    print('Jogador quer ser [1] par ou [2] impar?')
    j= int(input('R: '))
    a= randint(1,2)
    b= int(input('Escolha um Numero: '))
    if j == 1 and (a+b)%2 == 0:
        print ('\033[32m''Você venceu!!''\033[m')
    elif j == 1 and (a+b)%2 == 1:
        print('\033[31m''Você perdeu!!''\033[m')
    elif j == 2 and (a+b)%2 == 0:
        print('\033[31m''Você perdeu!!''\033[m')
    else:
        print ('\033[32mVocê venceu!!\033[m')



