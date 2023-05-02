def mnsg(m):
    print('-'*20)
    print(m)
    print('-'*20)

def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l:.2f}X{c:.2f} é de {a:.2f} m2.')

#Programa principal
mnsg('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)