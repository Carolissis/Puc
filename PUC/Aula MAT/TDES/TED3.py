print('\033[32m-'*30)
print(f'{"FUNÇÕES":^30}')
print('-'*30)
print('\033[m')

import matplotlib.pyplot as plt
import numpy as np

opcao = 0
while opcao != 3:
    print()
    opcao = int(input('\033[36m1- Função do 1º grau\n2- Função do 2º grau\n3- Sair\n R:\033[m'))
    if opcao == 1:
        perg1 = 0
        while perg1 != 4:
            print()
            perg1 = int(input('\033[36m1- A função é crescente ou decrescente\n2- Zero da função\n3-Gráfico da função\n4- Voltar\n R:\033[m'))
            if perg1 == 1:
                a = int(input('Termo "a": '))
                b = int(input('Termo "b": '))
                if a > 0:
                    print(f'\033[32mA função ƒ(x)={a}x+{b} é crescente\033[m')
                elif a < 0:
                    print(f'\033[32mA função ƒ(x)={a}x+{b} é decrescente\033[m')
                elif a == 0:
                    print(f'\033[32mA função ƒ(x)={a}x+{b} é reta\033[m')
            elif perg1 == 2:
                a = int(input('Termo "a": '))
                b = int(input('Termo "b": '))
                print(f'\033[32mO zero da função ƒ(x)={a}x+{b} é {b}\033[m')
            elif perg1 == 3:
                a = int(input('Termo "a": '))
                b = int(input('Termo "b": '))
                vetorX = np.arange(-10,10,0.1)
                vetorY = []
                def f(x):
                    y = a*x + 1
                    return y
                for x in vetorX:
                     vetorY.append(f(x))
                plt.plot(vetorX,vetorY, label = 'Função', color = 'g')
                plt.show()
    if opcao == 2:
        perg2 = 0
        while perg2 != 4:
            print()
            perg2 = int(input('\033[36m1- Saber as raízes\n2- Saber o vértice \n3-Gráfico da função\n4- Voltar\n R:\033[m'))
            if perg2 == 1:
                    a = int(input('Termo "a": '))
                    b = int(input('Termo "d": '))
                    c = int(input('Termo "c": '))
                    delta = b**2 + 4*a*c
                    if delta > 0:
                        print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes reais\033[m')
                        r1 = (-b + delta **(1/2))/ 2*a
                        r2 = (-b - delta **(1/2))/ 2*a
                        print(f'\033[32mAs raízes são {r1:.2f} e {r2:.2f}\033[m')
                    elif delta == 0:
                        print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 1 raíz real\033[m')
                        r = -b / (2*a)
                        print(f'\033[32mA raíz é {r:.2f}\033[m')
                    elif delta < 0:
                        print(f'\033[32mA função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes complexas\033[m')
            elif perg2 == 2:
                        a = int(input('Termo "a": '))
                        b = int(input('Termo "d": '))
                        c = int(input('Termo "c": '))
                        delta = b**2 + 4*a*c
                        xv = -b / (2*a)
                        yv = -(delta/(4*a))
                        print(f'\033[32mO vértice da função ƒ(x)={a}x^2+{b}x+{c} é ({xv:.2f}; {yv:.2f}\033[m) ')
            elif perg2 == 3:
                        a = int(input('Termo "a": '))
                        b = int(input('Termo "d": '))
                        c = int(input('Termo "c": '))
                        vetorX = np.arange(-20,20,0.1)
                        vetorY = []
                        def f(x):
                            y = a*(x**2)+ b*x + c
                            return y
                        for x in vetorX:
                            vetorY.append(f(x)) 
                        plt.plot(vetorX,vetorY, label = 'Função', color = 'g')
                        plt.show()

    if opcao == 3:
        print()
        print('\033[32mObrigada volte sempre :)\033[m')