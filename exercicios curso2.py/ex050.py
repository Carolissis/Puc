#Soma dos pares 
s = 0
count = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num %2 == 0:
        s += num
        count+= 1
        if count == 0:
            print('Não foram encontrados numeros pares, tente novamente')
print('Você informou {} números pares e a soma foi {}'.format(count, s))
