import umoeda

num = float(input('Digite um valor:\nR$'))
aum = int(input('Taxa de aumento: '))
des = int(input('Taxa de desconto: '))
print(f'O valor R${num:.2f} com um aumento de {aum}% é R${umoeda.aumentar(num, aum):.2f}')
print(f'O valor R${num:.2f} com um desconto de {des}% é R${umoeda.diminuir(num, des):.2f}')
print(f'O dobro de R${num:.2f} é R${umoeda.dobro(num):.2f}')
print(f'A metade de R${num:.2f} é R${umoeda.metade(num):.2f}')