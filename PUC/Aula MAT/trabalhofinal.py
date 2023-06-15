def conjuntos():
    A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
    B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())

    while True:
        print("\033[36m\nEscolha uma opção:")
        print("1. Verificar se A é subconjunto próprio de B")
        print("2. Realizar operação de União")
        print("3. Calcular intersecção")
        print("4. Calcular diferença")
        print("5. Sair\033[m")

        opcao = input()

        if opcao == '1': 
            if A < B:
                print("A é um subconjunto próprio de B.")
            else:
                print("A não é um subconjunto próprio de B.")
        elif opcao == '2':
            print(f"A união de A e B é:{A | B}") 
        elif opcao == '3':
            print(f"A intersecção de A e B é:{A & B}") 
        elif opcao == '4':
            print(f"A diferença de A e B é: {A - B}")  
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

import matplotlib.pyplot as plt
import numpy as np

def funcoes_2():
    a = int(input('Termo "a": '))
    b = int(input('Termo "d": '))
    c = int(input('Termo "c": '))

    while True:
        print("\033[36m\nEscolha uma opção:")
        print("1. Calcular as raízes")
        print("2. Calcular funcão em x pedido")
        print("3. Calcular o vértice")
        print("4. Gerar gráfico")
        print("5. Sair\033[m")

        opcao = input()

        if opcao == 1: 
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

        elif opcao == 2:
            x = int(input("Qual o valor de X?"))
            f = (a(x**2)+b*x+c)
            print(f'\033[32mO resultado é {f}\033[m')
        
        elif opcao == 3:
            delta = b**2 + 4*a*c
            xv = -b / (2*a)
            yv = -(delta/(4*a))
            print(f'\033[32mO vértice da função ƒ(x)={a}x^2+{b}x+{c} é ({xv:.2f}; {yv:.2f}\033[m) ')

        elif opcao == 4:
            def f(x, a, b, c):
                return a*x**2 + b*x + c

            x = np.linspace(-10, 10, 400)
            y = f(x, a, b, c)
            plt.figure(figsize=(8,6))
            plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.legend()
            plt.title('Gráfico da função quadrática')
            plt.show()
        
        elif opcao == 5:
            break 
        else:
            print("Opção inválida. Tente novamente.")

def funcao_exponencial():
    import matplotlib.pyplot as plt
    import numpy as np

    def f(x, a, b):
        return a * b**x

    a = float(input("Insira o valor do coeficiente a: "))
    b = float(input("Insira o valor do coeficiente b: "))

    while True:
        print("\033[36m\nEscolha uma opção:")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Calcular o vértice")
        print("4. Sair\033[m")

        opcao = input()
        
        if opcao == 1:
            if b > 1:
                print("A função é crescente.")
            elif 0 < b < 1:
                print("A função é decrescente.")
            else:
                print("Os valores inseridos para b não correspondem a uma função exponencial crescente ou decrescente.")

        elif opcao == 2:
            x = int(input("Qual o valor de X?"))
            print(f"f(x) = {f(x, a, b)}")

        elif opcao == 3:
            x = np.linspace(-10, 10, 400)
            y = f(x, a, b)

            plt.figure(figsize=(8,6))
            plt.plot(x, y, label=f'{a}*{b}^x')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.grid(True)
            plt.legend()
            plt.title('Gráfico da função exponencial')
            plt.show()
        
        elif opcao == 4:
            break 
        else:
            print("Opção inválida. Tente novamente.")

def matrizes():
    #continuar