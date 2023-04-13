num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
if 9 in num:
    print(f'Tem {num.count(9)} números 9')
else:
    print('O número 9 não foi digitado')

if 3 in num:
    print(f'O número 3 aparece na posição {num.index(3)}')

for n in num:
    if n % 2 == 0:
        print(f'O numero {n} é par')
