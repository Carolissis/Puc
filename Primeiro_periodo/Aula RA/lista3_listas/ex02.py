#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for c in range(10):
    num = int(input(f'Digite o {c+1} º valor: '))
    vetor.append(num)
vetor.sort(reverse= True)
print(vetor)