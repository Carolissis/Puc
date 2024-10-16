# Crie um programa que socilicita 6 números ao usuario, calcule a media,
# mostre ao usuario uma lista com os numeros iguais ou acima a media,
# e uma lista com os numeros abaixo da media

num = list()
soma = 0

for c in range(6):
    n = int(input(f'{c+1}° Número: '))
    num.append(n)
    soma += n

media = soma / 6
mai = []
men = []
for n in num:
    if n >= media:
        mai.append(n)
    else:
        men.append(n)

num.sort()
mai.sort()
men.sort()
print(f'A media da lista {num} é {media:.0f}')
print(f'Os valores igual ou acima da média são: {mai}')
print(f'Os valores abaixo da média são: {men}')
