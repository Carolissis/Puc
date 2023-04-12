
num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True: 
    x = int(input('Digite um número entre 0 e 20: '))
    if 0<= x <=20:
        print(f'Você digitou o número {num[x]}')
        y = str(input('Quer continuar?\n[S/N]\nR: ')).upper().strip()
        if y in 'N':
            break 
    else:
        print('Tente novamente.')
print('Muito obrigada :) até mais.')
