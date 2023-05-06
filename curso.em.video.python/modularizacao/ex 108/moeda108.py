# Arrumando o formato do preco do ex 107

import umoeda

num = float(input('Digite um valor:\nR$'))
aum = int(input('Taxa de aumento: '))
des = int(input('Taxa de desconto: '))
print(f'O valor {umoeda.moeda(num)} com um aumento de {aum}% é {umoeda.moeda(umoeda.aumentar(num, aum))}')
print(f'O valor {umoeda.moeda(num)} com um desconto de {des}% é {umoeda.moeda(umoeda.diminuir(num, des))}')
print(f'O dobro de {umoeda.moeda(num)} é {umoeda.moeda(umoeda.dobro(num))}')
print(f'A metade de {umoeda.moeda(num)} é {umoeda.moeda(umoeda.metade(num))}')