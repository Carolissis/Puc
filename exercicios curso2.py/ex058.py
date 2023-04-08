from random import randint

x = randint(0, 10)

print('Sou um computador...\npensei em um número de 0 a 10, tente advinhar!')
palpite = int(input('Palpite: '))

while palpite != x:
    if palpite > x:
        print('Mais baixo!')
        palpite = int(input('Palpite: '))
    if palpite < x:
        print('Mais alto!')
        palpite = int(input('Palpite: '))

print('Parabens, você advinhou!\nO número era {}'.format(x))
