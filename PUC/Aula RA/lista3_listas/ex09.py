#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
#elementos do vetor

lista = []
soma = 0
for n in range(10):
    num=int(input(f'Digite o {n+1}º valor: '))
    lista.append(num)
    quadrado = num * num 
    soma += quadrado
print(f'A soma dos quadrados dos numeros: ', end= '')
for e in lista:
    print(f'{e},',end='')
print(f'é igual a: {soma} ')