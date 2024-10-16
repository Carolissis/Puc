def imprimir(num):
    for n in range(1,num+1):
        for nu in range(1,n+1):
            print(nu,end=' ')
        print()

num = int(input('Digite um número: '))
imprimir(num)      