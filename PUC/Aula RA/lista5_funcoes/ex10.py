# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo
# um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3
# ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6,
# 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente

def jogo():
    from random import randint
    while True:
        j1 = randint(2,12)
        if j1 == 7 or j1 == 11:
            print(f'Parabens, você tirou {j1}, você é um natural ;)')
            break
        elif j1 == 2 or j1 == 3 or j1 == 12:
            print(f'CRAPS, você perdeu! Sua jogada deu {j1}')
            break
        else:
            print(f'Sua primeira jogada deu {j1}, agora tente acertar esse número de novo!')
            count = 2
            while True:
                j2 = randint(2,12)
                if j2 == 7:
                    print(f'Sua jogada deu {j2}, você perdeu')
                    break
                elif j1 != j2:
                    print(f'Sua {count}º jogada foi {j2} e a primeira foi {j1}, ainda não são iguais')
                    count +=1
                elif j1 == j2:
                    print(f'Parabens você ganhou! Sua 1º jogada foi igual a {count}º jogada, com o número {j1}')
                    break
        break      
print(jogo())