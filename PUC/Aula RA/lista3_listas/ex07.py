#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
soma = 0
mult = 1 
for n in range(5):
    num= int(input(f'{n+1}º número: '))
    lista.append(num)
    soma += num 
    mult *= num
lista.sort()
print(f'Os números adicionados foram {lista}')
print(f'A soma desses números é igual a {soma}\nA multiplicação desses números é igual a {mult}')