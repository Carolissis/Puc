#Ler o peso de cinco pessoas e falar qual foi o maior e qual foi o menor

menor = 0
maior = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da pessoa {}? '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}'.format(maior))
print('O menor peso lido foi de {}'.format(menor)) 
