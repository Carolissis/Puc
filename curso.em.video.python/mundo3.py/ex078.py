lista = [ ]


for i in range(1,6):
    num = int(input(f'Digite {i}º valor: '))
    lista.append(num)
maior = lista[0]
menor = lista[0]

for n in lista:
    if n > maior:
        maior = n
    if n < menor:
        menor = n 

print(f'A lista contem os seguintes valores: {lista}\nO maior valor é {maior}\nO menor é {menor}')