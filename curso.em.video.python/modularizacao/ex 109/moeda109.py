# Organizando formatcao 108

import umoeda

num = float(input('Digite um valor:\nR$'))
aum = int(input('Taxa de aumento: '))
des = int(input('Taxa de desconto: '))
print(f'O valor {umoeda.moeda(num)} com um aumento de {aum}% é {umoeda.aumentar(num, aum, True)}')
print(f'O valor {umoeda.moeda(num)} com um desconto de {des}% é {umoeda.diminuir(num, des, True)}')
print(f'O dobro de {umoeda.moeda(num)} é {umoeda.dobro(num, True)}')
print(f'A metade de {umoeda.moeda(num)} é {umoeda.metade(num, True)}')