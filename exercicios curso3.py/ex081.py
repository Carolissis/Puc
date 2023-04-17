# Digitar numeros, contar quantos, deixar na ordem decrescente e ver se o n 5 esta na lista 

r = 's'
lista = []

while r == 's':
    num = int(input('Digite um valor: '))
    lista.append(num)
    r = str(input('Deseja continua? \n[S/N]\nR: ')).lower().strip()
    
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 nao está na lista')