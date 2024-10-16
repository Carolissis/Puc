def imprimir(num):
    for n in range(1,num+1):
        print(f'{n} '*n)
 
num = int(input('Digite um número: '))
imprimir(num)