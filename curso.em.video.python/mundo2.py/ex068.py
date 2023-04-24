from random import randint

result = vit = 0
jogador = int(input('Escolha: \n[1] IMPAR\n[2] PAR\nR: '))

if jogador == 1:
    while True:
        x = randint(1, 10)
        y = int(input('Digite um número: '))
        result = x + y
        if result %2 == 1:
            print(f'Você venceu, o computador jogou {x}')
            vit += 1
        elif result %2 ==0:
            print(f'O computador venceu, ele jogou {x}, você teve {vit} vitórias')
            break 

if jogador == 2: 
    while True:
        x = randint(1, 10)
        y = int(input('Digite um número: '))
        result = x + y
        if result %2 == 0:
            print(f'Você venceu, o computador jogou {x}')
            vit+=1 
        elif result %2 == 1:
            print(f'O computador venceu, ele jogou {x}, você teve {vit} vitórias')
            break 


