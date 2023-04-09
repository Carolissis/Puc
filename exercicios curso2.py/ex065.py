quant = 0
média = 0 
maior = 0 
menor = 0 
soma = 0
resp = 's'

while resp in 's':
    n = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]')).lower().strip()
    quant +=1 
    soma += n
    média = soma / quant
    if quant == 1:
        menor = maior = n 
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor ))