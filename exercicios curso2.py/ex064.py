print('Digite um número [999 para parar]: ')

soma = 0 
vezes = 0
n = 0 

while n != 999:
    n = int(input('R: '))
    if n != 999:
        soma += n 
        vezes += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(vezes, soma))

