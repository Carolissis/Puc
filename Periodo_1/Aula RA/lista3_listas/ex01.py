#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
vetor = []
for c in range(5):
    num = int(input('Digite o 1º valor: '))
    vetor.append(num)
vetor.sort()
print(vetor)