def ler(num):
     x = 0
     for i in num:
          x +=1
     return x 

n = int(input('Digite um número: '))
n = str(n)
print(f'O número {n} tem {ler(n)} números')

